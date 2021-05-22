import itertools
from itertools import permutations

arr = ['3','3','3','3']
npr = itertools.permutations(arr,3)
ncr = itertools.combinations(arr,1)
print(len(list(ncr)))

