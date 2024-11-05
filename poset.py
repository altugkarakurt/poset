from collections.abc import Iterable
from utils import subset_order, powerset


class Poset:

    """----------------------------------------------------------------
    elems    : Elements in the partially ordered set
    cmp_func : A comparison function for ordering elements
        cmp_func(a,b) ->    1, if(a > b)
                      ->   -1, if(a < b)
                      ->    0, if(a = b)
                      -> None, if a and b are incomparable
    labels   : (Optional) Labels for elements, aligned with elems list.
               Default is str(elem)
    poset_str: (Optional) A short-hand label for the poset.
               Default is '{elems , cmp_func}'
    ----------------------------------------------------------------"""
    def __init__(self, elems, cmp_func=None, labels=None, poset_str=None):

        # This flag enables/disables order theoretic functionality such as
        # up-/down-set util functions. The elements in this poset are sets
        self.set_of_sets = isinstance(elems[0], Iterable)

        if(self.set_of_sets):
            self.elems = [set(s) for s in elems]
            self.labels = labels if(labels is not None) \
                          else [f"{{{','.join([str(si) for si in s])}}}" for s in elems]
        else:
            if(cmp_func is None):
                # If no ordering function is set, we assume it is subset
                # ordering. Then, the elements needs to be iterables.
                raise ValueError("A non-iterable base set passed with no custom ordering.")
            self.elems = elems
            self.labels = labels if(labels is not None) else [str(l) for l in elems]
        
        self.cmp_func = cmp_func if(cmp_func is not None) else subset_order
        self.poset_str = poset_str if(poset_str is not None) \
                         else f"({{{','.join(self.labels)}}}, {self.cmp_func.__name__})"

    def __repr__(self):
        return self.poset_str

    # Generate the elements as the powerset of a set of elements. If nonempty,
    # exclude the emptyset from the powerset
    @staticmethod
    def from_base_set(base_set, nonempty=True):
        elems = [] if(nonempty) else [[]]
        elems.extend(powerset(base_set))
        return Poset(elems, poset_str=(f"{{Powerset({','.join([str(s) for s in base_set])}), Subset-Order}}"))
