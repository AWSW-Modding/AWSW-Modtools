from algorithms.search import jaro_similarity

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
    
    for mod in modlist:
        name = mod[1]
        desc = mod[3]
        comps[name] = jaro_set_similarity(query_words, name, desc)
    
    return comps


def jaro_author_compare(author_query, modlist):
    comps = {}
    author_query = author_query.lower()
    
    for mod in modlist:
        name = mod[1]
        author = mod[2]
        comps[name] = jaro_similarity(author_query, author.lower())
    
    return comps


def sort_best(query, modlist, author_query="", return_score=False):
    """Sort mods by best match to query"""
    if query.strip():
        similarities = jaro_split_compare(query, modlist)
    else:
        similarities = {mod[1]: (0.0, 0.0) for mod in modlist}
    if author_query.strip():
        author_similarities = jaro_author_compare(author_query, modlist)
    else:
        author_similarities = {name: 0.0 for name in similarities.iterkeys()}
    similarities = {name: scores + (author_similarities[name],) for name, scores in
                    similarities.iteritems()}  # Much easier to deal with if it's a single iterable
    
    # Sort by best match, with bias to strong modname matches and strong authorname matches
    #  This bias is useful as the description normally takes the stronger value, unless the mod name is searched specifically.
    #  Max gave me better results than sum, so I used it.
    comp_func = lambda e: (max(e[1][:2]) + (int(e[1][0] > 0.9) * e[1][0]) + (int(e[1][2] > 0.7) * e[1][2]))
    mod_order = list(sorted(similarities.items(), key=comp_func, reverse=True))
    
    if comp_func(mod_order[0]) <= 0.3:  # All bad matches, don't reorder
        print "No good matches. reordering suppressed"
        mod_order = list((mod[1], 0.0) for mod in modlist)
    
    mods_by_name = {mod[1]: mod for mod in modlist}
    
    if return_score:
        return [(mods_by_name[name], score) for name, score in mod_order]
    else:
        return [mods_by_name[name] for name, _ in mod_order]


def clear_cache():
    _jaro_best_match_cache.clear()
    jaro_similarity.clear_cache()