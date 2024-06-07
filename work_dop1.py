import itertools
stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
area = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dict_ = {}
for subset in itertools.combinations(stuff, 2):
    for i in range(3, 6):
        list_name = [i]
        if i % sum(list(subset)) == 0:
            try:
                globals()[list_name].append(list(subset))
            except KeyError:
                globals()[list_name] = [i]
for i in range(20):
            # Print list_1 through list_20
            list_name = str(i)
            print(list_name + ' - ', globals()[list_name])
