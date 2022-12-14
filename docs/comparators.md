
Comparators


String comparators are algorithms used in data linkage to compare and evaluate the similarity between two strings of text. These algorithms can be applied to different types of data, including names, addresses, and other identifying information, to determine if two records refer to the same individual or entity.

One common use of string comparators in data linkage is to identify duplicates within a dataset. By comparing the strings of two records and calculating their similarity, the algorithm can flag records that may be duplicates and require further investigation. This can help to improve the accuracy and completeness of the data by eliminating incorrect or redundant information.

Another use of string comparators in data linkage is to merge different datasets or databases. By comparing strings across multiple sources, the algorithm can identify records that refer to the same individual or entity and merge them into a single record. This can be useful for creating a more comprehensive and accurate view of the data, and for identifying trends and patterns that may not be visible in a single dataset.


Jaro similarity


The Jaro measure is defined as the minimum of three values: the number of matching characters divided by the average length of the two strings, the number of transpositions divided by the average length of the two strings, and the number of matching characters divided by the maximum length of the two strings.

For example, the Jaro similarity between the strings "MARTHA" and "MARHTA" is 0.9444444444444444. This is calculated as follows: the number of matching characters is 6, the average length of the two strings is 6, the number of transpositions is 1, and the maximum length of the two strings is 7. Thus, the Jaro measure is calculated as 6 / 6 + 1 / 6 + 6 / 7 = 0.9444444444444444.


$m \leq \left\lfloor \frac{\min(|s|,|t|)}{2} \right\rfloor + \delta$

The Jaro similarity measure is often used in applications such as spell checking, entity resolution, and duplicate detection. It is particularly useful in cases where the two strings being compared are of similar length and contain similar characters. It is less effective, however, in cases where the two strings are very different in length or contain few common characters.


The formula for Jaro is:

$$Jaro = \frac{1}{3} \left[ \frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m-t}{m} \right]$$

where: 
$s_1$ and $s_2$ are the two strings being compared, 
$m$ is the number of common characters, 
and $t$ is the number of transpositions.







The formula for Jaro Winkler is:

$$Jaro Winkler = Jaro + p \cdot l \cdot (1 - Jaro)$$

where $Jaro$ is the Jaro similarity score, $p$ is the scaling factor, $l$ is the length of the common prefix, and $1 - Jaro$ is the penalty for non-matching characters at the beginning of the strings.








The Levenstein edit distance is a measure of the similarity between two strings of text. It is calculated by counting the number of operations (insertions, deletions, or substitutions) needed to transform one string into the other.


The formula for Levenstein Distance, also known as Edit Distance, is:

$$Levenstein(s_1, s_2) = \min \lbrace \begin{array}{l}
\text{insertion} \ ,
\text{deletion} ,
\text{substitution} 
\end{array} \rbrace $$

where $s_1$ and $s_2$ are the two strings being compared. This metric measures the minimum number of edit operations (insertions, deletions, and substitutions) required to transform one string into the other, and can be used to compare strings that may not be identical but are still similar.
