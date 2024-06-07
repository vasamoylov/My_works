import itertools
stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
area = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_ = []
#dict_ = {}
for subset in itertools.combinations(stuff, 2):
    for i in range(3, 6):
        if i % sum(list(subset)) == 0:
            #list_.append(list(subset))
            dic=dict.fromkeys([i],list(subset))
            for key, value in dic.items():
                print(key, '-', *value)
#print(list_)
