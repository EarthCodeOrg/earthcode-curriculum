# Permutations
import itertools
print(list(itertools.permutations('123')))

def permutations(iterable):
    if len(iterable) == 0:
        return []
    if len(iterable) == 1:
        return [iterable]
    perms = []
    for item in iterable:
        # for each set of permutations of len(iterable)-1 
        iterable_copy = iterable[:]
        iterable_copy.remove(item)
        for sub_perm in permutations(iterable_copy):
            perms.append( [item] + sub_perm )
    return perms
        
def permutations_iter(iterable):
    sub_permutations = {} # (1,2) : [(1,2),(2,1)]
    list_of_subsets_to_resolve = [iterable]
    while list_of_subsets_to_resolve:
        subset = list_of_subsets_to_resolve.pop()
        if len(subset) == 0:
            sub_permutations[subset] = []
        elif len(subset) == 1:
            sub_permutations[tuple(subset)] = [subset]
        else:
            n_subset_perms_resolved = 0
            for item in subset:
                subset_copy = subset[:]
                subset_copy.remove(item)
                if tuple(subset_copy) in sub_permutations:
                    n_subset_perms_resolved += 1
                else:
                    list_of_subsets_to_resolve.append(subset_copy) # [ ... , [1,2], [1],[2]]
                    
            if n_subset_perms_resolved == len(subset): 
                perms = []
                for item in subset:
                    subset_copy = list(subset[:])
                    subset_copy.remove(item)
                    subset_copy.sort()
                    for sub_perm in sub_permutations[tuple(subset_copy)]:
                        perms.append( tuple([item] + list(sub_perm)) )    
                sub_permutations[tuple(subset)] = perms
            else: 
                list_of_subsets_to_resolve.insert(-(len(subset)),subset)
    return sub_permutations[tuple(iterable)]