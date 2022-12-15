
# Comparators


String comparators are algorithms used in data linkage to compare and evaluate the similarity between two strings of text. These algorithms can be applied to different types of data, including names, addresses, and other identifying information, to determine if two records refer to the same individual or entity.

One common use of string comparators in data linkage is to identify duplicates within a dataset. By comparing the strings of two records and calculating their similarity, the algorithm can flag records that may be duplicates and require further investigation. This can help to improve the accuracy and completeness of the data by eliminating incorrect or redundant information.

Another use of string comparators in data linkage is to merge different datasets or databases. By comparing strings across multiple sources, the algorithm can identify records that refer to the same individual or entity and merge them into a single record. This can be useful for creating a more comprehensive and accurate view of the data, and for identifying trends and patterns that may not be visible in a single dataset.


## Jaro similarity


The Jaro measure is defined as the minimum of three values: the number of matching characters divided by the average length of the two strings, the number of transpositions divided by the average length of the two strings, and the number of matching characters divided by the maximum length of the two strings.

For example, the Jaro similarity between the strings "MARTHA" and "MARHTA" is 0.9444444444444444. This is calculated as follows: the number of matching characters is 6, the average length of the two strings is 6, the number of transpositions is 1, and the maximum length of the two strings is 7. Thus, the Jaro measure is calculated as 6 / 6 + 1 / 6 + 6 / 7 = 0.9444444444444444.


$m \leq \left\lfloor \frac{\min(|s_1|,|s_2|)}{2} \right\rfloor + \delta$

The Jaro similarity measure is often used in applications such as spell checking, entity resolution, and duplicate detection. It is particularly useful in cases where the two strings being compared are of similar length and contain similar characters. It is less effective, however, in cases where the two strings are very different in length or contain few common characters.


The formula for Jaro is:

$$Jaro = \frac{1}{3} \left[ \frac{m}{|s_1|} + \frac{m}{|s_2|} + \frac{m-t}{m} \right]$$

where: 
$s_1$ and $s_2$ are the two strings being compared, 
$m$ is the number of common characters, 
and $t$ is the number of transpositions.




## Jaro Winkler similarity


The formula for Jaro Winkler is:

$$Jaro Winkler = Jaro + p \cdot l \cdot (1 - Jaro)$$

where :

$Jaro$ is the Jaro similarity score, 
$p$ is the scaling factorfor how much the score is adjusted upwards for having common prefixes.$p$ should not exceed 0.25 
(i.e. 1/4, with 4 being the maximum length of the prefix being considered), otherwise the similarity could become larger than 1. The standard value for this constant in Winkler's work is $p$ = 0.1 )

$l$ is the length of the common prefix, 
and $1 - Jaro$ is the penalty for non-matching characters at the beginning of the strings.


## Levenstein edit distance 

The Levenstein edit distance is a measure of the similarity between two strings of text. It is calculated by counting the number of operations (insertions, deletions, or substitutions) needed to transform one string into the other.


The formula for Levenstein Distance, also known as Edit Distance, is:

$$Levenstein(s_1, s_2) = \min \lbrace \begin{array}{l}
\text{insertion} \ ,
\text{deletion} ,
\text{substitution} 
\end{array} \rbrace $$

where $s_1$ and $s_2$ are the two strings being compared. This metric measures the minimum number of edit operations (insertions, deletions, and substitutions) required to transform one string into the other, and can be used to compare strings that may not be identical but are still similar.

## Jaccard similarity 


The Jaccard similarity is a measure of similarity between two sets of data, and is often used in text analysis to compare the similarity of two documents. In this post, we will use the Jaccard similarity to compare the similarity of two addresses.

To start, we first need to break down each address into smaller substrings or "shingles". For example, let's say we have the following two addresses:

Address 1: 123 Main Street, Anytown USA

Address 2: 456 Elm Street, Anytown USA

We can break each address down into the following shingles:

Address 1: 123, Main, Street, Anytown, USA

Address 2: 456, Elm, Street, Anytown, USA

Next, we can use the Jaccard similarity formula to compare the similarity of these two addresses. The formula is as follows:

$$J(A,B)=\frac{|A \cap B|}{|A \cup B|}$$

Where $A$ and $B$ are the sets of shingles for each address, and $|A \cap B|$ is the number of elements that are common to both sets, and $|A \cup B|$ is the total number of elements in both sets.

In this example, the common elements between the two sets of shingles are "Street" and "Anytown". Therefore, the numerator of the Jaccard similarity formula is 2. The total number of elements in both sets is 6, so the denominator is 6. Therefore, the Jaccard similarity of these two addresses is $\frac{2}{6} = \frac{1}{3}$.

This means that these two addresses are only about 33% similar to each other, based on the shingles that we used in our analysis.


# Phonetic transformation algorithms

Soundex and Double Metaphone are algorithms for phonetic matching of words. This means that they can be used to match words that sound similar, even if they are spelled differently.

## Soundex

Soundex is a widely-used algorithm for phonetic matching. It was developed by Margaret K. Odell and Robert C. Russell in the early 1900s. The basic idea behind Soundex is to encode words based on their sounds, rather than their spelling. This allows words that sound similar to be encoded in the same way, even if they are spelled differently.

To encode a word with Soundex, the algorithm follows these steps:

```
Retain the first letter of the word.
Replace all other letters with the number 0.
Replace each of the following letters with the corresponding number:
B, F, P, V: 1
C, G, J, K, Q, S, X, Z: 2
D, T: 3
L: 4
M, N: 5
R: 6
```

For example, the name "John" would be encoded as "J500". The name "Gwion" would be encoded as "G500".

## Double Metaphone

Double Metaphone is a more advanced algorithm for phonetic matching, developed by Lawrence Philips in the 1990s. It is based on the Soundex algorithm, but is designed to be more accurate and to handle a wider range of words.

To encode a word with Double Metaphone, the algorithm follows these steps:

```
Retain the first letter of the word.
Remove any vowels, except for the first letter.
Replace certain letters with other letters or combinations of letters, as follows:
B: B
C: X if followed by "ia" or "h" (e.g. "Cia" becomes "X", "Ch" becomes "X"), otherwise "S"
D: J if followed by "ge", "gy", "gi", otherwise "T"
G: J if followed by "g", "d", "i", "y", "e", otherwise "K"
K: K
L: L
M: M
N: N
P: F
Q: K
R: R
S: X if followed by "h" (e.g. "Sh" becomes "X"), otherwise "S"
T: X if followed by "ia" or "ch" (e.g. "Tia" becomes "X", "Tch" becomes "X"), otherwise "T"
V: F
X: KS
Z: S
```

For example, the name "John" would be encoded as "JN". The name "Gwion" would be encoded as "JN".

In both cases, the names "John" and "Gwion" are encoded in the same way, because they sound similar even though they are spelled differently. This shows how Soundex and Double Metaphone can be used to match words that sound similar.


In conclusion, Soundex and Double Metaphone are useful phonetic transformations for tasks such as spelling correction and name matching. By encoding words into standardized codes based on their phonetic sound, these algorithms can help improve accuracy and efficiency in these tasks.


