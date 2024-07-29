first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = (len(x[0]) - len(x[1]) for x in list(zp) if len(x[0]) - len(x[1]) != 0)
second_result = (len(x) == len(y) for x in first for y in second if first.index(x) == second.index(y))

print(list(first_result))
print(list(second_result))