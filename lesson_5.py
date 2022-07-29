import datetime as dt
import json


start_prog = dt.datetime.now()

'''
for i in range(10000):
    print(i)

end_prog = dt.datetime.now()
print(end_prog - start_prog)


res = []


def div(number):
    return True if number % 2 == 0 else False


    for i in range(100):
        if len(res) == 5:
            break
        else:
            if div(i) == True:
                res.append(i)
            else:
                pass
print(res)

while True:                   # operator break - this case more preferably
    input_value = input('enter quit if u want stop: ')
    if input_value == 'quit':
        break
    else:
        print(input_value)

input_value = input('enter quit if u want stop: ')
while input_value != 'quit':
    input_value = input('enter quit if u want stop: ')
    print(input_value)
'''

'''
for i in range(1, 100):               # Var 1
    if i % 5 == 0:
        continue
    else:
        print(i)

for i in range(1, 100):               # var 2
    if i % 5 == 0:
        pass
    else:
        print(i)


def check_div_and_cont(enter_range: int) -> None:     # because we haven't return
    for i in range(int(enter_range)):  # var 2
        if i % 2 == 0:
            continue
        else:
            print(i)


print(check_div_and_cont(100))


def args_example(*args):      # * "pack - unpack" function
    help_list = list(args)
    print(type(args))
    for i in help_list:
        print(i)


print(args_example([5, 3, 5]))        # args - always tuple
print(args_example(*(5, 3, 5)))
print(args_example(*(5, 3, 5)), args_example(12, 4, 6, 7, 8, 9, 12))
'''


# file input/output

# f = open('new_file.txt', 'x')    # 'x' - create new file
# print(f.read())                  # read ('way.extention', 'r')
# f.write('some text')             # 'r' - read, 'a' - append,
# f.close()

# with open('way.extention', 'r') as f:
# print(type(f.readline()))


# json        : format: key-value

obj = {'name': 'Arthur Conan Doyle',
       'books': [{'name': 'The Hound of the Baskervilles'},
                 {'name': 'The Leather Funnel'}]}

print(json.dumps(obj))
print(type(json.dumps(obj)))

print(obj.keys())
print(obj['name'], obj['books'])
for i in obj['books']:
    print(i)

'''
a_input = input('enter value: ')
b_input = input('enter second value: ')

try:
    a_input = int(a_input)
    b_input = int(b_input)
    print(a_input / b_input)
except ValueError:
    print('Try Again!')
else:
    print(a_input)
'''

name_of_city = input('enter city: ')


def check_input_city(name:str) -> str:
    # 1
    return ''.join(i for i in name if i.isalpha() or i in [' ', '-']).capitalize()
    # 2
    # res = ''
   # for i in name:
    #    if i.isalpha() or i in ['', '-']:
    # res = res + i
    #        ....save

name_clear = (check_input_city(name_of_city))
print(name_clear)


def get_weather(name:str, api:str):
    try:
        url_api = f'https://api.openweathermap.org/data/2.5/weather?q={name_clear}&appid={api_name}&units=metric'
        response = requests.get(url_api)
        data_json = response.json()
        return data_json['main']['temp']
    except:
        print('Wrong name api, or wrong name city')

api_name = '33d99a1c99c5ea82e6aaff8592cd6fc3'
des_input = input('Enter something to continue else enter stop: ')
while des_input != 'stop':

    name_of_city = input('Input City:')
    name_clear = check_input_city(name_of_city)
    print(f'Weather in city {name_clear} is {get_weather(name_clear, api= api_name)}')
    des_input = input('Enter something to continue else enter stop: ')


input_des = input('Enter stop to stop or press any: ')
    while input_des != 'stop':
   # input_des = int('Enter start: ')
        try:
            input_a = int(input('Enter int: '))
            input_des = input('Enter stop to stop or press any: ')
        except:
            print('Try again!')
            input_des = input('Enter stop to stop or press any:: ')
        else:
            print(input_a)



'''
# bonus
def rle(string):
    string = string + ' '
    result = ''
    counter = 1
    for i in range(0, len(string) - 1):
        if string[i] == string[i+1]:
            counter += 1
        elif string[i] != string[i+1]:
            result = result + string[i] + str(counter)
            counter = 1
    return result
'''