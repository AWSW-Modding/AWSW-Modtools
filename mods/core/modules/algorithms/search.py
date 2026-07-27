
# This file contains function definitions from nltk repository, under the Apache License Version 2.0
# in particular, the function jaro_similarity has been used.
# Those have been used under these attributions:
#
# Copyright (C) 2001-2025 NLTK Project
# Author: Edward Loper <edloper@gmail.com>
#         Steven Bird <stevenbird1@gmail.com>
#         Tom Lippincott <tom@cs.columbia.edu>
# URL: <https://www.nltk.org/>
# For attribution license information, see NLTK_LICENSE.txt
#
# All components which are not explicitly licensed under the Apache License Version 2.0 of nltk (NLTK_LICENSE.txt) are original to this project, and licensed under this project's standard license (LICENSE)
#

def cache(function):
    def inner(*args):
        if not hasattr(inner, "results"):
            inner.results = {args: function(*args)}
        elif args not in inner.results:
            inner.results[args] = function(*args)
        return inner.results[args]
    def clear_cache():
        if hasattr(inner, "results"):
            inner.results.clear()
    inner.clear_cache = clear_cache
    return inner

# Copied from nltk (https://www.nltk.org/_modules/nltk/metrics/distance.html#jaro_similarity)
# This function is copied from nltk, and is therefore licensed under their Apache License Version 2.0 (NLTK_LICENSE.txt)
@cache
def jaro_similarity(s1, s2):
    """
    Computes the Jaro similarity between 2 sequences from:

        Matthew A. Jaro (1989). Advances in record linkage methodology
        as applied to the 1985 census of Tampa Florida. Journal of the
        American Statistical Association. 84 (406): 414-20.

    The Jaro distance between is the min no. of single-character transpositions
    required to change one word into another. The Jaro similarity formula from
    https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance :

        ``jaro_sim = 0 if m = 0 else 1/3 * (m/|s_1| + m/s_2 + (m-t)/m)``

    where
        - `|s_i|` is the length of string `s_i`
        - `m` is the no. of matching characters
        - `t` is the half no. of possible transpositions.
    """
    # First, store the length of the strings
    # because they will be re-used several times.
    len_s1, len_s2 = len(s1), len(s2)
    
    # The upper bound of the distance for being a matched character.
    match_bound = max(int(max(len_s1, len_s2) / 2) - 1, 0) # My change from the original algorithm: allows two length=1 words to match if they are the same word.
    
    # Initialize the counts for matches and transpositions.
    matches = 0  # no.of matched characters in s1 and s2
    transpositions = 0  # no. of transpositions between s1 and s2
    flagged_1 = []  # positions in s1 which are matches to some character in s2
    flagged_2 = []  # positions in s2 which are matches to some character in s1
    
    # Iterate through sequences, check for matches and compute transpositions.
    for i in range(len_s1):  # Iterate through each character.
        upperbound = min(i + match_bound, len_s2 - 1)
        lowerbound = max(0, i - match_bound)
        for j in range(lowerbound, upperbound + 1):
            if s1[i] == s2[j] and j not in flagged_2:
                matches += 1
                flagged_1.append(i)
                flagged_2.append(j)
                break
    flagged_2.sort()
    for i, j in zip(flagged_1, flagged_2):
        if s1[i] != s2[j]:
            transpositions += 1
    
    if matches == 0:
        return 0
    else:
        matches = float(matches) # Added to nltk's implementation. int division and float division are qualitatively different in python 2 (unlike python 3, where nltk is implemented), and the float division is the intended behaviour.
        return (
                1 / 3.0 # Changed from nltk's 3 to 3.0, for the same reason as the last change.
                * (
                        matches / len_s1
                        + matches / len_s2
                        + (matches - int(transpositions / 2)) / matches
                )
        )



