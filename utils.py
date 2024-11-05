from itertools import chain, combinations


# Generates the set of all non-empty subsets of a set of elements
def powerset(base_set):
    return chain.from_iterable(combinations(base_set, r) for r in range(1,len(base_set)+1))

# Compares Iterables using subset order, returns None if incomparable
def subset_order(s1, s2):
    if((s1_s2 := s1.issubset(s2)) and (s2_s1 := s2.issubset(s1))):
        return 0 # S1 = S2
    elif(s1_s2):    
        return -1 # S1 subset S2, S1 < S2
    elif(s2_s1):
        return 1 # S2 subset S1, S1 > S2
    else:
        return None # S1,S2 are incomparable
