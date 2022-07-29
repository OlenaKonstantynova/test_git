# homework_1

'''
                # exersice 1 from  hw 1
name = str(input('name '))
salary = int(input('salary '))
print(name + '\'s annual salary is ' + str((salary * 12) // 1000) + ' thousand dollars')
'''

'''
                # exersice 2 from hw 1
even_number_100_999 = int(input('number = '))      # input the integer number
# 1 var
print(even_number_100_999 % 2 == 0 and 100 < even_number_100_999 < 999)                # check conditions

# 2 var
if even_number_100_999 % 2 == 0 and 100 < even_number_100_999 < 999:
    print('True')
else:
    print('False')
'''

'''
                # exersice 3 from hw 1
n_1 = int(input('enter a three-digit integer: '))
# 1
n_2 = 0
while n_1 > 0:
    digit = n_1 % 10        # find a remainder
    n_1 = n_1 // 10         # divide without remainder to remove the last digit
    n_2 = n_2 * 10          # increase the digit capacity of the second number
    n_2 += digit            # add the last digit
print('The "inverse" of the number: ', n_2)

# 2
n_1_list = list(str(n_1))
n_2 = n_1_list[::-1]
print('The "inverse" of the number: ', n_2)
'''

'''
                # exersice 4 from hw 1
num_1 = int(input('enter first integer number: '))
num_2 = int(input('enter second integer number: '))
sum_num = num_1 + num_2                                      # a) - sum of numbers
print(sum_num)
dif_num = num_1 - num_2                                      # b) - difference of numbers
print(dif_num)
mult_num = num_1 * num_2                                     # c) - multiplication of numbers
print(mult_num)
div_num = num_1 / num_2 if num_2 != 0 else 'division by 0 is not possible'     # d) - division of numbers
print(div_num)
rem_num = num_1 % num_2 if num_2 != 0 else 'division by 0 is not possible'     # e) - remainder of division
print(rem_num)
comperison = 'true' if num_1 >= num_2 else 'false'                             # f) - comparison of numbers - V1
print(comperison)
print(num_1 >= num_2)                                                          # f) - comparison of numbers - V2
'''

# exersice from 1 lecture
'''
                # Exersice 5 from lesson 1
a = int(input('length= '))      # a - input the rectangle's length
b = int(input('width= '))       # b - input the rectangle's width
area = a * b                    # the rectangle’s area
perimeter = 2 * (a + b)         # the rectangle’s perimeter
print('the rectangle’s area = ' + str(area) + ', ' + 'the rectangle’s perimeter = ' + str(perimeter))
'''

'''
                # Exersice 6 from lesson 1
even_number = int(input('number = '))      # input the integer number
# 1 var
print(even_number % 2 == 0)                # even check

# 2 var
if even_number % 2 == 0:
    print('True')
else:
    print('False')
'''

'''
                 # Exersice 7 from lesson 1
odd_number = int(input('number = '))      # input the integer number
# 1 
print(odd_number % 2 == 1)                # odd check

# 2 
if odd_number % 2 == 1:
    print('True')
else:
    print('False')
'''

'''
                # Exersice 8 from lesson 1
div_by_16_22 = int(input('number = '))                      # input the integer number
# 1
print(div_by_16_22 % 16 == 0 and div_by_16_22 % 22 == 0)    # dividing by 16 and 22
# 2
if div_by_16_22 % 16 == 0 and div_by_16_22 % 22 == 0:
    print('True')
else:
    print('False')
'''