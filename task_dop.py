def calculate_list(list_):
    summa_l = int()
    for l in list_[0:]:
        if type(l) == int:
            summa_l = summa_l + int(l)
        elif type(l) == str:
            summa_l = int(summa_l) + len(l)
        elif type(l) == list:
            summa_l = summa_l + calculate_list(l)
        elif type(l) == tuple:
            summa_l = summa_l + calculate_list(l)
    return summa_l

def calculate_dict(dict_):
    summa_d = int()
    list_key = dict_.keys()
    for key in list_key:
        if type(key) == int:
            summa_d = summa_d + int(key)
        elif type(key) == str:
            summa_d = summa_d + len(key)
    list_value = dict_.values()
    for value in list_value:
        if type(value) == int:
            summa_d = summa_d + int(value)
        elif type(value) == str:
            summa_d = summa_d + len(value)
    return summa_d
def calculate_structure_sum(area):
    summa = int()
    if type(area) == list or set or tuple:
        for i in area[0:]:
            if type(i) == int:
                summa = int(i)
                area.remove(i)
            elif type(i) == str:
                summa = int(summa) + len(i)
                area.remove(i)
            elif type(i) == list:
                summa = summa + calculate_list(i)
            elif type(i) == dict:
                summa = summa + calculate_dict(i)
            elif type(i) == tuple:
                summa = summa + calculate_list(i)
            elif type(i) == set:
                list_s = list(i)
                summa = summa + calculate_list(list_s)
        for i in area[0:][0:]:
            if type(i) == int:
                summa = int(i)
                area.remove(i)
            elif type(i) == str:
                summa = int(summa) + len(i)
                area.remove(i)
            elif type(i) == list:
                summa = summa + calculate_list(i)
                area.remove(i)
            elif type(i) == dict:
                summa = summa + calculate_dict(i)
                area.remove(i)
            elif type(i) == tuple:
                summa = summa + calculate_list(i)
                if calculate_list(i) > 0:
                    area.remove(i)
                else:
                    continue
            elif type(i) == set:
                list_s = list(i)
                summa = summa + calculate_list(list_s)
        for i in area[0][0][0:]:
            if type(i) == set:
                list_s = list(i)
                for j in list_s[0:][0:]:
                    if type(j) == int:
                        summa = summa + int(j)
                        list_s.remove(j)
                    elif type(j) == str:
                        summa = int(summa) + len(j)
                        list_s.remove(j)
                    elif type(j) == list:
                        summa = summa + calculate_list(j)
                    elif type(j) == dict:
                        summa = summa + calculate_dict(j)
                    elif type(j) == tuple:
                        summa = summa + calculate_list(j)
        for i in area[0][1][0:]:
            if type(i) == set:
                list_s = list(i)
                for j in list_s[0:][0:]:
                    if type(j) == int:
                        summa = summa + int(j)
                        list_s.remove(j)
                    elif type(j) == str:
                        summa = int(summa) + len(j)
                        list_s.remove(j)
                    elif type(j) == list:
                        summa = summa + calculate_list(j)
                    elif type(j) == dict:
                        summa = summa + calculate_dict(j)
                    elif type(j) == tuple:
                        summa = summa + calculate_list(j)

    return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
