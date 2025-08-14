from functools import reduce

def sum(x, y):
    return x + y

numbers_list = [1, 3, 5, 10, 20]
sum_result = reduce(sum, numbers_list)

print(sum_result)