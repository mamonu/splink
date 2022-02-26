from copy import deepcopy

from .blocking import block_using_rules
from .comparison_vector_values import compute_comparison_vector_values
from .maximisation_step import compute_new_parameters


def _num_target_rows_to_rows_to_sample(target_rows):
    # Number of rows generated by cartesian product is
    # n(n-1)/2, where n is input rows
    # We want to set a target_rows = t, the number of
    # rows generated by Splink and find out how many input rows
    # we need to generate targer rows
    #     Solve t = n(n-1)/2 for n
    #     https://www.wolframalpha.com/input/?i=Solve%5Bt%3Dn+*+%28n+-+1%29+%2F+2%2C+n%5D
    sample_rows = 0.5 * ((8 * target_rows + 1) ** 0.5 + 1)
    return sample_rows


def estimate_u_values(linker, target_rows):

    original_settings_object = linker.settings_obj
    training_linker = deepcopy(linker)

    training_linker.train_u_using_random_sample_mode = True

    settings_obj = training_linker.settings_obj
    settings_obj._retain_matching_columns = False
    settings_obj._retain_intermediate_calculation_columns = False
    for cc in settings_obj.comparisons:
        for cl in cc.comparison_levels:
            cl._level_dict["tf_adjustment_column"] = None

    sql = """
    select count(*) as count
    from __splink__df_concat_with_tf
    """
    dataframe = training_linker.sql_to_dataframe(sql, "__splink__df_concat_count")
    result = dataframe.as_record_dict()
    count_rows = result[0]["count"]

    if settings_obj._link_type in ["dedupe_only", "link_and_dedupe"]:
        sample_size = _num_target_rows_to_rows_to_sample(target_rows)
        proportion = sample_size / count_rows

    if settings_obj._link_type == "link_only":
        sample_size = target_rows**0.5
        proportion = sample_size / count_rows

    if proportion >= 1.0:
        proportion = 1.0

    if sample_size > count_rows:
        sample_size = count_rows

    sql = f"""
    select *
    from __splink__df_concat_with_tf
    {training_linker.random_sample_sql(proportion, sample_size)}
    """
    print(sql)
    training_linker.execute_sql(
        sql,
        "__splink__df_concat_with_tf_sample",
        "__splink__df_concat_with_tf_sample",
        transpile=False,
    )

    settings_obj._blocking_rules_to_generate_predictions = []

    sql = block_using_rules(training_linker)
    training_linker.enqueue_sql(sql, "__splink__df_blocked")

    sql = compute_comparison_vector_values(settings_obj)

    training_linker.enqueue_sql(sql, "__splink__df_comparison_vectors")

    sql = """
    select *, 0.0D as match_probability
    from __splink__df_comparison_vectors
    """
    training_linker.enqueue_sql(sql, "__splink__df_predict")

    sql = compute_new_parameters(settings_obj)
    training_linker.enqueue_sql(sql, "__splink__df_new_params")

    df_params = training_linker.execute_sql_pipeline()

    param_records = df_params.as_record_dict()

    m_u_records = [
        r for r in param_records if r["comparison_name"] != "_proportion_of_matches"
    ]

    for record in m_u_records:
        cc = original_settings_object._get_comparison_by_name(record["comparison_name"])
        gamma_val = record["comparison_vector_value"]
        cl = cc.get_comparison_level_by_comparison_vector_value(gamma_val)

        cl.add_trained_u_probability(
            record["u_probability"], "estimate u by random sampling"
        )

    training_linker.train_u_using_random_sample_mode = False
