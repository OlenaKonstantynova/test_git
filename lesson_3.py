arr = [12, 4, 5, 6]
# arr.index(-1)
arr.sort()
# arr[::-1]
list_test = ['a', 'z', 'b', 'c', 'e']
list_test.sort()
print(list_test)

len(list_test)

# arr + list_test
s = arr + list_test
print(s)
# s.sort()

arr.extend(list_test)
arr.append(12)
print(arr)

# del - delete by index
# remove -delete by value

arr = [12, 34, 31, 12, 4]
new_arr = []
for i in arr:
    if i != 12:
        new_arr.append(i)

for i in range(0, len(arr)):
    if arr[i] == 3:
        arr.remove(12)
print(arr)

second_list = ['a', 'b', 'c', 'e', 'v']
for items in second_list:
    print(items)

for items in str(14):
    print(items)

# str - combine тип ,int - simple type

print(list(range(0, 10)))
print(list(range(10)))
print(list(range(0, 10, 2)))

new_list_for_ave = [3, 5, 8, 7, 12, 0, 1, 23, -5, 56]
if len(new_list_for_ave) == 10:
    # print(new_list_for_ave)
    counter = 0
    counter_len = 0
    for i in new_list_for_ave:
        counter += i
    for i in new_list_for_ave:
        counter_len += 1

print(sum(new_list_for_ave) / len(new_list_for_ave))


for i in range(1, 1000):
    if i % 14 == 0:
        print(i)

x = (1, 2, 3, 4, 4)  # - tuple  - no changed  ordered type - faster because of hashing, list - changed ordered type
y = (5, 6, 7)
print(x)
tmp = list(x)
tmp.append(6)
print(tuple(tmp))

print(x + y)
print(x * 2)
print(sorted(x))

# set - no ordered collection of data
colors = {12, 5, 6, 12, 8}
colors.add('red')  # by element
colors.update('wer')   # add several elements
print(colors)


n = 200
i = 2
primfac = []
while i * i <= n:
    while n % i == 0:
        primfac.append(i)
        n = n / i
    i = i + 1
if n > 1:
    primfac.append(n)
print(primfac)

# .remove (value)
# .discard (value)
# .pop (value) - last value

d = dict()
d['Sasha'] = 'Ukrainets'
d[0] = 'Dima'
d[17] = (1, 2)

for key, value in d.items():
    print(key, value)
'''
for value in d.value():
    print(value)

for key in d.keys():
    print(key)
'''

dictionary = dict()
dictionary['Kyiv'] = ['044']
dictionary['Sumy'] = ['056']
dictionary['Lviv'] = ['075']
dictionary['Kharkiv'] = ['030']
dictionary['Crimea'] = ['015']
print(list(dictionary.keys()))

pattern_k = []
for i in list(dictionary.keys()):

    if i[0] in ['k', 'K']:
        pattern_k.append(dictionary[i])
print(pattern_k)

pattern_k = []
for i in list(dictionary.keys()):

    if 'v' in i or 'V' in i:
        pattern_k.append(dictionary[i])
print(pattern_k)

student = dict()
student['Genna'] = 5
student['Maria'] = 4.8
student['Vlad'] = 4.554
student['Alex'] = 5.0
student['Vika'] = 4.92

print(student)

counter_student_mark = 0
help_len = 0
for value in student.values():
    help_len += 1
    counter_student_mark += value
print(counter_student_mark / help_len)


print(sum(list(student.values())) / len(student))

comp_res = [i for i in student.values() if i != 5]
print(comp_res)
