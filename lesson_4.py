# import frame
# import random
# from python_lessons.python


def test(a):
    return True if 118 < a <= 27 else False


print(test(27))

arr = [1, 3, 5, 7, 90, -1]
print(sum(arr), max(arr), min(arr))

counter = 0
max_of = 0
min_of = 0
for i in arr:
    if i > max_of:
        max_of = i
    elif i < min_of:
        min_of = i
    counter += i
print(counter, max_of, min_of)
# [::-1] == reversed

# print(random.randint(0,10))


def mean(x):
    return sum(x) / len(x)


print(mean((1, 3, 4, 6, 7)))


def mean(x: list) -> float:
    return sum(x) / len(x)


print(mean((1, 3, 4, 6, 7)))


def summ_of(arr: list) -> float:
    counter = 0
    for i in arr:
        counter += i
    print(counter)
    return sum(arr)


print(summ_of([4, 5, 6, 7, 2, 9]))


def div_of(arr):
    # 1
    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    return res

    # 2
    return [i for i in arr if i % 2 == 0]


print(div_of(list(range(1, 51))))


def hello_name(name: str):
    return 'Hello ' + name + '\nHave a good day!'


print(hello_name('Olena'))


def hello_name_sur(name: str = 'test', surname: str = 'test'):
    return 'Hello ' + name + ' ' + surname + '\nHave a good day!'


print(hello_name_sur('Olena', 'Konstantynova'))

mean_t = lambda x: sum(x) / len(x)
summ_lambda = lambda x: x + 1

print(summ_lambda(mean_t([1, 2, 5, 6, 9])))

plus_of_number = lambda a, b: a + b
list_of_number = [1, 2, 5, 6, 9]

print(plus_of_number(list_of_number[1], list_of_number[3]))

minus_of_number = lambda a, b: a - b
mult_of_number = lambda a, b: a * b

print(minus_of_number(list_of_number[1], list_of_number[3]))
print(mult_of_number(list_of_number[1], list_of_number[3]))

student = [5, 6, 7, 1, 5, 4]
mean_of_user_mark = mean(student)
for i in student:
    if i > mean_of_user_mark:
        print('Big', i)
    elif i < mean_of_user_mark:
        print('Small', i)
    elif i == mean_of_user_mark:
        print('Equal', i)

first_a = [1, 2, 3, 4, 5]
second_b = ['a', 'b', 'c', 'd', 'e']
print(list(zip(first_a, second_b)))  # equals count of elements

third_c = [1, 34, 5, 6, 9]
if len(first_a) == len(second_b) == len(third_c):
    print(list(zip(first_a, second_b, third_c)))
else:
    print('add new element')

if len(first_a) == len(second_b) == len(third_c):
    result = list(zip(first_a, second_b, third_c))
    res = []
    for i in result:
        res.append(list(i))
    print(res)
else:
    print('add new element')

# from my_project.lesson_4 import ()

# math

import math as math
print(math.sqrt(9), math.e, math.pi)

print(math.sqrt(9) == 9 ** 0.5, math.pow(4, 2) == 4 ** 2)

stroka = 'some, some,,, 12%'
print(stroka.split(','))
print(''. join(i for i in stroka if i.isdigit() or i.isalpha()))

stroka_dva = '!18,21,56,78,aa'.replace('aa', '12').lstrip('!')
print([int(i) for i in stroka_dva.split(',')])

stroka_name = 'OlekSanDR'
print(stroka_name.capitalize(), stroka_name.lower())
print('{0}, {1}'.format(12, 4))
print(f'{12} + {5} = {12 + 5}')

string_list = 'Sasha, Alex, Oleksandr, Dima, Olya, Maria'
string_list_mark = '5,3,5,4,5,5'. split(',')

list_new_mark = [int(i) for i in string_list_mark]
print(list_new_mark)
avg_mark = mean(list_new_mark)
min_mark = min(list_new_mark)
max_mark = max(list_new_mark)
mediana = list_new_mark[len(list_new_mark) // 2]
print(avg_mark, min_mark, max_mark, mediana)


import datetime as dt

print(dt.datetime.now())
