# sentence = 'This is a string in single quotes'
# print(sentence)
from turtledemo.sorting_animate import instructions1

# sentence = "This is a string in double quotes"
# print(sentence)

# str_a = """This is a multiline string
# Line 1 added
# Line 2 added
# Line 3 added
# Line 4 added
# Line 5 added
# """
# print(str_a)

# str_b = '''This is a multiline string using triple quote notation with single quote
# Line 1 added
# Line 2 added
# Let's close this string
# '''
# print(str_b)
# a = "This is a longer string"
# print(a[1], a[2], a[10])

# print(str_b)

# Let's try to modify str_b now, it will give a runtime error
# str_b[10]='S'

# first_name = 'Jane'
# last_name = 'Doe'
# print(first_name + last_name)
# print(first_name + ' ' + last_name)
# print('{} {}'.format(first_name, last_name))

# print(type(987653))

# fval = 10.54
# print(fval)
# print(type(fval))

# fval2 = 5.64e-5
# print(fval2)
# print(type(fval2))

# print(4/3)
# print(type(4/3))

# is_true = True
# is_false= False
# print(is_true, is_false)

# print(is_true and is_false)
# print(is_true or is_false)

# small = 10
# big = 20
# print("small + big = ",small + big)
# print("small - big = ",small - big)
# print("small * big = ",small * big)
# print("small / big = ", big / small)
# print("small // big = ",big // small)
# print("small % big = ",big % small)

# admin_password = 1234
# user_input = 1234
# print(admin_password == user_input)
# print(admin_password != user_input)

# print(small == big)
# print (small != big)

# username = input('Enter your username: ')
# print(username)

# print(small / big)
# print (small % big)
# print(small ** big)
# print(small // big)
# print(big // small)
# print((small+big) / big)

# print('=========')

# print(small > big)
# print(small < big)
# print(small >= big)
# print(small <= big)
# print(small != big)

# print(-5 / 2)

# password = '1234'
# if password == '1234':
#     print('password is correct')
# else:
#     print('password is incorrect')

# fruit = input('Enter your fruit? ')
# if fruit == 'orange':
#     print('I do not really like oranges')
# elif fruit == 'apple':
#     print('apples are my favorite')
# else:
#     print('hmm I might also like ' + fruit)

# first_name = input('Enter your first name? ')
# last_name = input('Enter your last name? ')
# if first_name == 'Jane' and last_name == 'Doe':
#     print('Welcome, ' + first_name + ' ' + last_name)
# else:
#     print('User not recognised')

# name = input('Enter your name ')
# if name == 'Carl' or name == 'Carlson':
#     print('Hello, ' + name)
# else:
#     print('You are not Carl')


# stored_name = 'Scrat'
# stored_password = 'nuts'
# supplied_name = input('Please enter your username ==> ')
# supplied_password = input('Please enter your password ==> ')
# if supplied_name == stored_name and supplied_password == stored_password:
#     print('Welcome, ' + stored_name)
# else:
#     print('Sorry User with name ' + supplied_name + ' and Password ' + supplied_password + ' does not exist')

# def say_hi():
#     return('Hello and welcome to my program')
# print(say_hi())

# def say_hi(name):
#     return f'Hello and welcome to my program, {name}!'
# print(say_hi('Sarah'))

# def add_optional_bonus(num1,num2,opt1=0,opt2=0):
#     return num1+num2+opt1+opt2

# print(add_optional_bonus(5,6))
# print(add_optional_bonus(5,6,opt2=5))
# print(add_optional_bonus(5,6,opt2=6))
# print(add_optional_bonus(5,6,opt2=6,opt1=5))

# def next_three_values(start_num):
#     a = start_num + 1
#     b = start_num + 2
#     c = start_num + 3
#     return a, b, c


# x, y, z = next_three_values(100)
# print(x, y, z)

# stored_name = 'Scrat'
# stored_pword = 'nuts'


# def test_name(name):
#     if name == stored_name:
#         return True
#     else:
#         return False
#

# def test_pword(pword):
#     if pword == stored_pword:
#         return True
#     else:
#         return False


# input_name = input('Enter Username ==> ')
# input_pword = input('Enter Password ==> ')

# if test_name(input_name) and test_pword(input_pword):
#     print('Welcome ' + stored_name)
# elif test_name(input_name) or test_pword(input_pword):
#     print('Incorrect username or password')
# else:
#     print('Incorrect username and password')

# myFruitList = ['apple', 'banana', 'pear']
# print(myFruitList)

# print(myFruitList[0])
# print(myFruitList[1])
# print(myFruitList[2])

# print(myFruitList[-1])

# myFruitList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'banana']
# print(myFruitList[0:3])
# print(myFruitList[3])

# print(len(myFruitList))

# print(len(set(myFruitList)))

# myFruitList= ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'banana']
# print(myFruitList)
# myFruitList.append('pear')
# myFruitList.remove('cherry')
# print(myFruitList)

# myFruitList= ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'banana']
# myFruitList[1] = 'strawberry'
# print(myFruitList)

# list_one = [1, 2, 3]
# list_two = [4, 5, 6]
# list_three = list_one + list_two
# print(list_three)

# shopping_list = ['bread', 'milk', 'cereals', 'donuts', 'snacks']
# for i in shopping_list:
#     print(i)
# print()
# for items in shopping_list:
#     print(items)
# print()
# counter = 0
# while counter < 3:
#     counter+=1
#     print(counter)

# to_do_list = []
# Instructions = """To-Do list  Generator
# Enter each memo in turn
# Hit enter (with no data) when list is complete"""
# print(Instructions)
# list_item = input('==> ')
# while list_item != '':
#     to_do_list.append(list_item)
#     list_item = input('==> ')
# for item in to_do_list:
#     print(item)
# print (23 % 2)

# primes=[]
# valid=True
# print('Calculating prime numbers from 1 to 100')
# for outer in range(1,101):
#     print (outer)
#     for inner in range(2,outer):
#         valid=True
#         if outer % inner == 0:
#             valid=False
#             break

    # if valid:
    #     primes.append(outer)
# print(primes)

finished=False
instructions = """Simple Calculator
Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Multiplication
Enter 4 for Division
Enter 5 to Exit calculator"""

def add(a,b):
    print (f'{a} plus {b} = {a + b}')

def sub(a, b):
    print (f'{a} minus {b} = {a - b}')

def mult(a, b):
    print (f'{a} times {b} = {a * b}')

def div(a, b):
    if b == 0:
        print ("can't divide by zero")
    else:
        print (f'{a} divided by {b} = {a / b}')

while not finished:
    print(instructions)
    choice=input('Enter your choice: ')
    if not choice in ('1','2','3','4','5'):
        print('Invalid input')
    elif choice == '5':
        print('BYE')
        finished=True
    else:
        a=float(input('Enter first number: '))
        b=float(input('Enter second number: '))
        if choice == '1':
            add(a,b)
        elif choice == '2':
            sub(a,b)
        elif choice == '3':
            mult(a,b)
        else:
            div(a,b)