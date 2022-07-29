# homework_2

'''
# exersice_1
num_3_5 = int(input('number = '))               # input the integer number
if num_3_5 % 3 == 0 and num_3_5 % 5 != 0:       # checking divisibility by 3 and non-divisibility by 5
    print('foo')
elif num_3_5 % 5 == 0 and num_3_5 % 3 != 0:     # checking divisibility by 5 and non-divisibility by 3
    print('bar')
elif num_3_5 % 3 == 0 and num_3_5 % 5 == 0:     # checking divisibility by 3 and by 5
    print('ham')
else:                                           # in all other cases, the number is not divisible by 3 or 5
    print('number is not divisible by 3 or 5')
'''


'''
# exersice_2
a = float(input('first number = '))
b = float(input('second number = '))
if (a - b) > 0:                                 # if the result of subtraction is positive, then
    print('first number > second number')                                # the first number is greater than the second
elif (a - b) < 0:                               # if the result of subtraction is negative, then
    print('first number < second number')                                # the first number is less than the second
else:                                           # in all other cases the numbers are equal
    print('first number = second number')
'''

'''
# exersice_3
a = float(input('first number = '))
b = float(input('second number = '))
c = float(input('third number = '))

# 1
max_abc = (a if a > b else b) if (a if a > b else b) > c else c       # compare two numbers, find the larger, then compare with the third
print('the biggest number is ' + str(max_abc))
min_abc = (a if a < b else b) if (a if a < b else b) < c else c       # compare two numbers, find the smaller, then compare with the third
print('the lowest number is ' + str(min_abc))
if a <= b <= c or c <= b <= a:                                        # find the middle number if one of the two inequalities is satisfied
    print('the middle number is ' + str(b))
elif b <= a <= c or c <= a <= b:                                      # check each of the three numbers
    print('the middle number is ' + str(a))
else:
    print('the middle number is ' + str(c))

# 2
numbers = [a, b, c]                                                  # create the list with three entered numbers
print('the lowest number is ' + str(sorted(numbers)[0]))             # sorted this list
print('the middle number is ' + str(sorted(numbers)[1]))             # find the lowest, middle, biggest number with index
print('the biggest number is ' + str(sorted(numbers)[2]))            # [0] - lowest, [1] - middle, [2] - biggest number
'''

'''
# 5
numbers_1_100 = list(range(1, 101))
fizz_buzz = []                                                      # create empty list
for element in numbers_1_100:                                       # loop through all elements
    if element % 3 == 0 and element % 5 != 0:                       # checking divisibility by 3 and non-divisibility by 5
        fizz_buzz.append('fizz')                                    # add new element 'fizz' to fizz_buzz list if conditions are met
    elif element % 5 == 0 and element % 3 != 0:                     # checking divisibility by 5 and non-divisibility by 3
        fizz_buzz.append('buzz')                                    # add new element 'buzz' to fizz_buzz list if conditions are met
    elif element % 3 == 0 and element % 5 == 0:                     # checking divisibility by 3 and 5
        fizz_buzz.append('fizz buzz')                               # add new element 'fizz buzz' to fizz_buzz list if conditions are met
    else:                                                           # in all other cases add an element from the list numbers_1_100 without changes
        fizz_buzz.append(element)

print(fizz_buzz)
'''
