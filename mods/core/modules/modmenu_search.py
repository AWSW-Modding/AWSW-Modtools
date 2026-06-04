
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
    match_bound = max(int(max(len_s1, len_s2) / 2) - 1, 0) # My one change from the original algorithm: allows two length=1 words to match if they are the same word.
    
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



_jaro_best_match_cache = {}


def jaro_set_similarity(query_set, target1, target2):
    """Finds approximate similarity between word set query_set and target word strings target1 and target2.
    each word in query_set is compared against all of target1's and target2's words to find the best match.
    the similarity is then the average of each of those best similarity numbers.
    these results are cached by target1 for each word of query_set, and as such, for each value of target1 there should only be a single value of target2."""
    
    
    best_similarity_1 = {}
    best_similarity_2 = {}
    for query_word in query_set:
        if (query_word, target1) not in _jaro_best_match_cache:
            t1_word_set = set(target1.lower().split())
            curr_best_1 = 0
            for target_word in t1_word_set:
                curr_best_1 = max(curr_best_1, jaro_similarity(query_word, target_word))
            best_similarity_1[query_word] = curr_best_1
            
            t2_word_set = set(target2.lower().split())
            curr_best_2 = 0
            for target_word in t2_word_set:
                curr_best_2 = max(curr_best_2, jaro_similarity(query_word, target_word))
            best_similarity_2[query_word] = curr_best_2
            
            _jaro_best_match_cache[(query_word, target1)] = (curr_best_1, curr_best_2)
        else:
            sim1, sim2 = _jaro_best_match_cache[(query_word, target1)]
            best_similarity_1[query_word] = sim1
            best_similarity_2[query_word] = sim2
    
    n_values = len(query_set)
    return (sum(best_similarity_1[query_word] for query_word in query_set) / n_values,
            sum(best_similarity_2[query_word] for query_word in query_set) / n_values)



def jaro_split_compare(query, modlist):
    """Compare the modlist to the query using jaro similarity on each word.
    :returns dict from modname to similarity tuple, which contains the similarity of query to modname, then the similarity of query to mod description.
    """
    comps = {}
    query_words = set(query.lower().split())
    
    for _, name, _, desc, _ in modlist:
        comps[name] = jaro_set_similarity(query_words, name, desc)
    
    return comps

def jaro_author_compare(author_query, modlist):
    comps = {}
    author_query = author_query.lower()
    
    for _, name, author, _, _ in modlist:
        comps[name] = jaro_similarity(author_query, author.lower())
    
    return comps


def sort_best(query, modlist, author_query="", return_score=False):
    """Sort mods by best match to query"""
    if query.strip():
        similarities = jaro_split_compare(query, modlist)
    else:
        similarities = {name: (0.0, 0.0) for _, name, _, _, _ in modlist}
    if author_query.strip():
        author_similarities = jaro_author_compare(author_query, modlist)
    else:
        author_similarities = {name: 0.0 for name in similarities.iterkeys()}
    similarities = {name: scores + (author_similarities[name],) for name, scores in similarities.iteritems()} # Much easier to deal with if it's a single iterable
    
    # Sort by best match, with bias to strong modname matches and strong authorname matches
    #  This bias is useful as the description normally takes the stronger value, unless the mod name is searched specifically.
    #  Max gave me better results than sum, so I used it.
    comp_func = lambda e: (max(e[1][:2]) + (int(e[1][0] > 0.9) * e[1][0]) + (int(e[1][2] > 0.7) * e[1][2]))
    mod_order = list(sorted(similarities.items(), key=comp_func, reverse=True))
    
    if comp_func(mod_order[0]) <= 0.3: # All bad matches, don't reorder
        print "No good matches. reordering suppressed"
        mod_order = list((name, 0.0) for _, name, _, _, _ in modlist)
    
    mods_by_name = {mod[1]: mod for mod in modlist}
    
    if return_score:
        return [(mods_by_name[name], score) for name, score in mod_order]
    else:
        return [mods_by_name[name] for name, _ in mod_order]
    

def clear_cache():
    _jaro_best_match_cache.clear()
    jaro_similarity.clear_cache()