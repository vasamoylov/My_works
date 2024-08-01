def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        list_divider = [x for x in range(2, summ // 2 + 1) if summ % x == 0]
        if len(list_divider) == 0:
            print('Простое')
        else:
            print('Составное')
        return summ
    return wrapper

@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)

