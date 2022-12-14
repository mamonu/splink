

The formula for Jaro is:

$$Jaro = \frac{1}{3} \left[ \frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m-t}{m} \right]$$

where $s_1$ and $s_2$ are the two strings being compared, $m$ is the number of common characters, and $t$ is the number of transpositions.







The formula for Jaro Winkler is:

$$Jaro Winkler = Jaro + p \cdot l \cdot (1 - Jaro)$$

where $Jaro$ is the Jaro similarity score, $p$ is the scaling factor, $l$ is the length of the common prefix, and $1 - Jaro$ is the penalty for non-matching characters at the beginning of the strings.




The formula for Levenstein Distance, also known as Edit Distance, is:

$$Levenstein(s_1, s_2) = \min \lbrace \begin{array}{l}
\text{insertion} \
\text{deletion} \
\text{substitution}
\end{array} \right}$$

where $s_1$ and $s_2$ are the two strings being compared. This metric measures the minimum number of edit operations (insertions, deletions, and substitutions) required to transform one string into the other, and can be used to compare strings that may not be identical but are still similar.
