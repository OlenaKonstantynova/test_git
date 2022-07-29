# pickle

import pickle
from functools import reduce
from collections import defaultdict, Counter
from itertools import permutations, combinations
from itertools import product

# Создание и вписывание данных(шаг 1)
name_with_mark = {'Name1': 90, 'Name2': 98, 'Name3': 60, 'Name4': 76, 'Name5': 81}

pickle_out = open('dict.pickle', 'wb')  # создать pickle
pickle.dump(name_with_mark, pickle_out)  # вписать в него значение словаря
pickle_out.close()  # закрыть файл

# После шага один(закоментировать код)
# Шаг два - разпаковка данных
pickle_in = open('dict.pickle', 'rb')
new_name = pickle.load(pickle_in)  # создали словарь

print(new_name.keys())  # можно работать как с обычным словорем


# filter
def div_value(item):
    return True if item % 2 == 0 else False


def change_minus(item):
    return item * -1


def check_string(item):
    return True if item in ['a', 'b', 'c'] else False

# def


string = 'adhfbckl'

print(list(filter(check_string, string)))

a = list(range(50))
b = list(filter(div_value, a))
c = list(filter(lambda x: x % 2 == 1, a))
print(b)
print(c)

# map
a_map = list(range(-50, 50))
print(a_map)
b_map = list(map(lambda x: x ** 2, a_map))
print(b_map)
c_map = list(map(change_minus, a_map))
print(c_map)

# reduce

a_reduce = [14, 5, 6, 7, 3, 4, 1, 12, 68, -10]
string_reduce = ['s', 'a', 's', 'c', 'h', 'a']
b_reduce = reduce(lambda x, y: x + y, a_reduce)
print(b_reduce)
c_reduce = reduce(lambda x, y: x + y, string_reduce)
print(c_reduce)


# recursion - a function calling itself

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


# OOP
# Object-oriented programming in Python

class Transport:
    """
    class descr transport type
    """
    def __init__(self, name, weight, mark):
        self.name = name
        self.weight = weight
        self.mark = mark

    def print_info(self):
        return f'Hello {self.name} u strong {self.mark}'


obj_a = Transport(name='bus', weight=4000, mark='Bogdan')
print(obj_a.print_info())
print(obj_a.name)
print(obj_a.weight)
print(obj_a.mark)

obj_b = Transport(name='Train', weight='300000', mark='Hundai')
print(obj_b.print_info())

# function and options and properties of class - read!!!

# defaultdict
'''
d = defaultdict(lambda: [])
d[‘a’].append(100)
print(d[‘a’])
'''

# counter
# input_some_text = input('Enter name: ')
input_some_text = 'Vadim'
name_list = ['sasha', 'vadim']
some_r = [1, 2, 4, 5, 6, 6]
counter = Counter(input_some_text)
print(counter)
print(Counter(some_r))


# product
print(list(product(some_r, name_list)))

dna = 'abc'
print(list(permutations(dna)))

# combinations
print(list(combinations(some_r, 3)))

# algorithms
arr = [34, 50, 101, 67, 87]        # brute force
for i in arr:
    if i == 101:
        print(arr.index(i))
        break      # if we want to find first element

# binary search algorithm
