import collections


# Copied from nltk (https://www.nltk.org/_modules/nltk/metrics/distance.html#jaro_similarity)
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
    match_bound = int(max(len_s1, len_s2) / 2) - 1
    
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
        matches = float(matches)
        return (
                1 / 3.0
                * (
                        matches / len_s1
                        + matches / len_s2
                        + (matches - int(transpositions / 2)) / matches
                )
        )

def jaro_counter_similarity(query_counter, target_counter):
    """Finds approximate similarity between word counter query_counter and word counter target_counter.
    each word in query_counter is compared against all of target_counter's words to find the best match.
    the similarity is then the weighted average of each of those best similarity numbers, weighted by word count in query_counter"""
    
    best_similarity = {}
    for query_word in query_counter.iterkeys():
        curr_best = 0
        for target_word in target_counter.iterkeys():
            curr_best = max(curr_best, jaro_similarity(query_word, target_word))
        best_similarity[query_word] = curr_best
    
    return sum(best_similarity[query_word] * count for query_word, count in query_counter.iteritems()) / sum(query_counter.itervalues())
    
def jaro_split_compare(query, modlist):
    """Compare the modlist to the query using jaro similarity on each word.
    :returns dict from modname to similarity tuple, which contains the similarity of query to modname, then the similarity of query to mod description.
    """
    comps = {}
    query_words = collections.Counter(query.lower().split())
    
    for _, name, _, desc, _ in modlist:
        name_words = collections.Counter(name.lower().split())
        name_similarity = jaro_counter_similarity(query_words, name_words)
        
        desc_words = collections.Counter(desc.lower().split())
        desc_similarity = jaro_counter_similarity(query_words, desc_words)
        
        comps[name] = (name_similarity, desc_similarity)
    
    return comps


def sort_best(query, modlist, return_score = False):
    """Sort mods by best match to query"""
    similarities = jaro_split_compare(query, modlist)
    
    mod_order = [entry for entry in sorted(similarities.items(), key=lambda e: max(e[1]), reverse=True)]
    
    mods_by_name = {mod[1]: mod for mod in modlist}
    
    if return_score:
        return [(mods_by_name[name], score) for name, score in mod_order]
    else:
        return [mods_by_name[name] for name, _ in mod_order]
    
