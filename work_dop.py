import itertools
from collections import defaultdict
from functools import reduce

list_ = []
list_2 = []
for subset in itertools.combinations(range(1, 21), 2):
    for i in range(3, 21):
        if i % sum(list(subset)) == 0:
            list_.append(list(subset))
            dic = dict.fromkeys([i], list(subset))
            list_2.append(dic)

def foo(r, d):
    for k in d:
        r[k].append(d[k])

d = reduce(lambda r, d: foo(r, d) or r, list_2, defaultdict(list))
for j in d:
    if len(d[j]) > 1:
        result = sum(d[j], [])
        print(j, result)
    else:
        result = sum(d[j], [])
        print(j, result)
