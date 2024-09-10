<<<<<<< HEAD
'''Hello world
#Hello world
print ('Hello world!')

'''

'''Variable
#Variable is a container for value. Behave as a value that contains
first_name = "Deepakraj"
last_name = "Teekaraman"
full_name = first_name +" "+ last_name
print(type(full_name))   
print ("Hello "+full_name)
'''

'''integer,float,boolean
#integer (Not assign value within quotes, technically it will become string, can only concanate string with string so use type change)
age = 24
age += 1
print (type(age))
print ("your age is: "+ str(age))

#float
height = (280.55)
print (height)
print (type(height))
print ("Your height is: "+str(height)+" cm")

#boolean
human = False
print (type(human))
print(human)
'''

'''Multiple assignments
#Multiple assignments in python. This will help in assigning multiple variables to one line of code at same time
name, age, height = 'deepakraj', 24, 245.55
print(name+" "+str(age)+" "+str(height))
'''

'''String methods
#String methods in python
name = 'deepakraj teekaraman'

print (len(name)) #length of the string
print (name.find("a")) #find place of the string
print (name.capitalize()) #capitalise
print (name.upper()) #turns upper
print (name.lower()) #turns lower
print (name.isdigit()) #checks for digit
print (name.isalpha()) #check for alphabet
print (name.count("e")) #count e
print (name.replace("e","o")) #replace the alphabet
print (name*3) 
'''

'''Type casting
#Type casting = convert the data type of value to another data type
x = 1
y = 2.0
z = "3"

y = int(y)

print (float(x))
print (y)
print (z)
'''

'''user input in python
#user input in python
first_name = str(input("what is your first_name? "))
last_name = str (input ("what is your last_name? "))
name = first_name + last_name
age = int(input("what is your age? "))

print("Hello! "+ name + " your are  "+ str(age)+ " years old")
'''

'''import math
#import math (funtions for number)
import math 
pi = 3.14
x = 1
y =2
z = 3

print (round(pi)) #round the value
print (math.ceil(pi)) #round it off to next values
print (math.floor(pi)) #round it off to previous values
print (abs(pi)) #gives absolute value
print (pow(pi)) #The pow() function returns the value of x to the power of y (xy).
print (math.sqrt(pi)) #sqrt func
print (max(x,y,z))
print (min(x,y,z))
'''

'''string slicing 
#string slicing in python = create a substring by extracting elements from another string
#indexing[] or slice()
#[start:stop:step]
name = "deepakraj teekaraman"
first_name = name[0:10] #cut from 0 to 9, if you leave out 0 and write like :3, it will automatically consider the first index as 0
last_name = name[10:]
funky_name = name[0:20:3] #the 3 in the end meaning every 3rd string
reversed_name = name[::-1] #will reverse the name

print (first_name)
print (last_name)
print (funky_name)
print (reversed_name)

web = "http://google.com"
slice = slice(7,-4)
print(web[slice])
'''

'''If statement 
#If statement = a block of statement that will execute if it's true
age = int(input("what is your age?: "))

if age == 100:
    print ("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age <= 5:
    print ("You are a child")
else:
    print("you are not an adult")
'''

'''Logical operators
#Logical operators in python (and,or,not)
temp = int(input("what is the temperature? "))

if temp >= 0 and temp <=30:
    print("the temperature is good today")
elif temp < 0 or temp >30:
    print ("It's not that good")
'''

'''while loop   
#while loop = a statement that execute it's block of code, as long as it's condition is true
name = ""
while len(name) == 0:
    name = input("enter your name: ")
print("hello! "+name)
'''

'''for loop
#for loop in python = a statement that will execute it's block of code a limited amount of times
#while loop = unlimted
#for loop = limited

#for i in range(10):
#     print(i)

#for i in range(50,100):  #first number is inclusive and second number is exclusive
#    print(i)

#for i in "Deepakraj":
#    print(i)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print ("Happy new year!")
'''

'''Nested loops
#Nested loops = the inner loop will finish all of the iterartions before finsihing one iteraton of outer loop
rows = int(input("How many rows?:"))
coulmns = int(input("how many coulmns?:"))
symbol = input("symbol")

for i in range(rows):
    for j in range(coulmns):
        print(symbol, end="") #will end and won't got to next line
  print() #to print in the next line

''' 

'''Loop control statements
#Loop control statements = change a loops execution from it's normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

while True:
    name = input("name?")
      if name!= "":
        break

phone_number = "123-456-7890"

for i in phone_number:
   if i == "-":
       continue
    print(i, end="")

for i in range (1,20):

    if i ==13:
        pass
    else:
        print(i,end="")

''' 

'''List
#List = used to store multiple items in a single variable

food = ["pizza","doner","Ham"]

food [0] = "Briyani"

food.append("icecream")
food.remove("Ham")
food.pop() #will remove last element
food.insert(0,"cake")
food.sort() #sort list alphabetically
food.clear() #will remove all the elements

for x in food:
    print (x)

'''

'''2D lists
#2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","briyani"]
dessert = ["cake","icecream"]

food = [drinks,dinner,dessert]

print(food[0][1])

'''

'''Tuples
#Tuples = collection which is ordered and unchangable, used to group together related data

student = ("john",21,"male")

print(student.count("john"))
print(student.index("male"))

for x in student:
    print(x)

if "john" in student:
    print("john is here")

'''

'''set
#set = collection which is unordered, unindexed, no duplicate values, faster than lists

utensils = {"fork","spoon","knife"}
dishes={"bowl","plate","cup","spoon"}

utensils.update(dishes)

utensils.add("napkin")
utensils.remove("spoon")
utensils.clear

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) #will check for differences
utensils.intersection(dishes) #will return common element

for x in dinner_table:
    print(x)

'''

'''Dictionary
#Dictionary = a changable, unordered collection of unique key:value pairs, fast because they use hashing, allow us to access a value quickly

capitals = {'USA' : 'DC', 'india':'delhi', 'germany':'berlin'}
print(capitals['USA'])

capitals.update({'france':'paris'})
capitals.update({'USA':'Vegas'})
capitals.pop('germany')

#print(capitals.get['germany'])
print(capitals.keys())
print(capitals.values())
print(capitals.items())

'''

'''index operator
#index operator [] = gives access to a sequence's elemnt (str,list,tuples)

name = "Deepak raj!"

if (name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[6:-1].upper()
last_char = name[-1]
print(first_name,last_name,last_char)

'''

'''Function
#Function = a block of code which is executed only when it is called

def hello(first_name,last_name,age):
    print ("Hello! "+first_name+" "+last_name)
    print ("You are "+str(age)+" years old")
    print ("Have a nice day")

hello("Deepakraj","Teekaraman","21") #info that are being sent to function are arguments needs matching number of parameters
'''

'''Return_statement
#Return_statement = functions send python values/object back to the caller
#                   These values/objects are known as the function's return value

def multiply(num1,num2):
    return num1*num2

x = multiply(6,8)
print(x)
'''

'''Keyword arguments
#Keyword arguments = Arguments preceded by an identifier when we pass them to a funtion
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    python knows the names of the arguments that out funtion recieves

def hello(first,middle,last):
    print("Hello "+first+middle+" "+last)

hello(middle="raj",last="Teekaraman",first="deepak")
'''

'''Nested_funtion_calls
#Nested_funtion_calls = func calls inside other func calls
#                       innermost func calls are resolved first
#                        returned values is used as argument for the next outer function

num = input("Enter a whole postive number: ")
num = float(num)
num = abs(num)
num = round(num)
print (num)

num = round(abs(float(input("Enter a number: "))))
print (num)
'''

'''Scope
#Scope = The region that a variable is recognized
#        A variable is only available from inside the region it is created
#        A global locally scoped versions of a variable can be created
#        Follows L=Local, E= Enclosing, G=Global, B= built in

name = "Raj" #global scope (available inside and outside of function)

def display_name():
    name = "Deepak" #local scope(available only inside this funtion)
    print(name)

display_name()
print(name)
'''

'''Args
#Args = parameter that will pack all arguments into a tuple
#       useful so that a function can be accept a varying amount of arguments

def add(*sum_values):
    sum = 0
    sum_values = list(sum_values) #casted tuple to list to change the values
    sum_values[0] = 15
    for i in sum_values:
        sum +=i
    return sum

print (add(1,2,3,4,5))
'''

'''*kwargs
#*kwargs = parameter that will pack all arguments into a dictionary
#          useful so that a function can accept a varying amount of keywords

def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print (value,end=" ")

hello (title="Mr.",first = "Deepak",middle="raj",last="Teekaraman")
'''

'''str.format()
#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

name = "Deepak"

print("hello, my name is {}".format(name))
print("hello, my name is {:10}. Nice to meet you".format(name))
print("hello, my name is {:>10}. Nice to meet you".format(name))
print("hello, my name is {:<10}. Nice to meet you".format(name))
print("hello, my name is {:^10}. Nice to meet you".format(name))

text = "The {} jumped over the {}"
print (text.format(animal,item))

number = 3.141594
print ("The number pi is {:.2f}".format(number))
print ("The number pi is {:,}".format(number))
print ("The number pi is {:b}".format(number))
print ("The number pi is {:o}".format(number))
print ("The number pi is {:X}".format(number))
print ("The number pi is {:E}".format(number))

#print ("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow","moon"))
print("The {0} jumped over the {1}".format("cow","moon")) #positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword arguemnt
'''

'''Random variable
import random #pseudo-random

x = random.randint(1,6)
y = random.random()

mylist = ['rock','paper','scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
cards = random.shuffle(cards)

print(cards)

print(x)
print(y)
print(z)
'''

=======
'''Hello world
#Hello world
print ('Hello world!')

'''

'''Variable
#Variable is a container for value. Behave as a value that contains
first_name = "Deepakraj"
last_name = "Teekaraman"
full_name = first_name +" "+ last_name
print(type(full_name))   
print ("Hello "+full_name)
'''

'''integer,float,boolean
#integer (Not assign value within quotes, technically it will become string, can only concanate string with string so use type change)
age = 24
age += 1
print (type(age))
print ("your age is: "+ str(age))

#float
height = (280.55)
print (height)
print (type(height))
print ("Your height is: "+str(height)+" cm")

#boolean
human = False
print (type(human))
print(human)
'''

'''Multiple assignments
#Multiple assignments in python. This will help in assigning multiple variables to one line of code at same time
name, age, height = 'deepakraj', 24, 245.55
print(name+" "+str(age)+" "+str(height))
'''

'''String methods
#String methods in python
name = 'deepakraj teekaraman'

print (len(name)) #length of the string
print (name.find("a")) #find place of the string
print (name.capitalize()) #capitalise
print (name.upper()) #turns upper
print (name.lower()) #turns lower
print (name.isdigit()) #checks for digit
print (name.isalpha()) #check for alphabet
print (name.count("e")) #count e
print (name.replace("e","o")) #replace the alphabet
print (name*3) 
'''

'''Type casting
#Type casting = convert the data type of value to another data type
x = 1
y = 2.0
z = "3"

y = int(y)

print (float(x))
print (y)
print (z)
'''

'''user input in python
#user input in python
first_name = str(input("what is your first_name? "))
last_name = str (input ("what is your last_name? "))
name = first_name + last_name
age = int(input("what is your age? "))

print("Hello! "+ name + " your are  "+ str(age)+ " years old")
'''

'''import math
#import math (funtions for number)
import math 
pi = 3.14
x = 1
y =2
z = 3

print (round(pi)) #round the value
print (math.ceil(pi)) #round it off to next values
print (math.floor(pi)) #round it off to previous values
print (abs(pi)) #gives absolute value
print (pow(pi)) #The pow() function returns the value of x to the power of y (xy).
print (math.sqrt(pi)) #sqrt func
print (max(x,y,z))
print (min(x,y,z))
'''

'''string slicing 
#string slicing in python = create a substring by extracting elements from another string
#indexing[] or slice()
#[start:stop:step]
name = "deepakraj teekaraman"
first_name = name[0:10] #cut from 0 to 9, if you leave out 0 and write like :3, it will automatically consider the first index as 0
last_name = name[10:]
funky_name = name[0:20:3] #the 3 in the end meaning every 3rd string
reversed_name = name[::-1] #will reverse the name

print (first_name)
print (last_name)
print (funky_name)
print (reversed_name)

web = "http://google.com"
slice = slice(7,-4)
print(web[slice])
'''

'''If statement 
#If statement = a block of statement that will execute if it's true
age = int(input("what is your age?: "))

if age == 100:
    print ("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age <= 5:
    print ("You are a child")
else:
    print("you are not an adult")
'''

'''Logical operators
#Logical operators in python (and,or,not)
temp = int(input("what is the temperature? "))

if temp >= 0 and temp <=30:
    print("the temperature is good today")
elif temp < 0 or temp >30:
    print ("It's not that good")
'''

'''while loop   
#while loop = a statement that execute it's block of code, as long as it's condition is true
name = ""
while len(name) == 0:
    name = input("enter your name: ")
print("hello! "+name)
'''

'''for loop
#for loop in python = a statement that will execute it's block of code a limited amount of times
#while loop = unlimted
#for loop = limited

#for i in range(10):
#     print(i)

#for i in range(50,100):  #first number is inclusive and second number is exclusive
#    print(i)

#for i in "Deepakraj":
#    print(i)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print ("Happy new year!")
'''

'''Nested loops
#Nested loops = the inner loop will finish all of the iterartions before finsihing one iteraton of outer loop
rows = int(input("How many rows?:"))
coulmns = int(input("how many coulmns?:"))
symbol = input("symbol")

for i in range(rows):
    for j in range(coulmns):
        print(symbol, end="") #will end and won't got to next line
  print() #to print in the next line

''' 

'''Loop control statements
#Loop control statements = change a loops execution from it's normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

while True:
    name = input("name?")
      if name!= "":
        break

phone_number = "123-456-7890"

for i in phone_number:
   if i == "-":
       continue
    print(i, end="")

for i in range (1,20):

    if i ==13:
        pass
    else:
        print(i,end="")

''' 

'''List
#List = used to store multiple items in a single variable

food = ["pizza","doner","Ham"]

food [0] = "Briyani"

food.append("icecream")
food.remove("Ham")
food.pop() #will remove last element
food.insert(0,"cake")
food.sort() #sort list alphabetically
food.clear() #will remove all the elements

for x in food:
    print (x)

'''

'''2D lists
#2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","briyani"]
dessert = ["cake","icecream"]

food = [drinks,dinner,dessert]

print(food[0][1])

'''

'''Tuples
#Tuples = collection which is ordered and unchangable, used to group together related data

student = ("john",21,"male")

print(student.count("john"))
print(student.index("male"))

for x in student:
    print(x)

if "john" in student:
    print("john is here")

'''

'''set
#set = collection which is unordered, unindexed, no duplicate values, faster than lists

utensils = {"fork","spoon","knife"}
dishes={"bowl","plate","cup","spoon"}

utensils.update(dishes)

utensils.add("napkin")
utensils.remove("spoon")
utensils.clear

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) #will check for differences
utensils.intersection(dishes) #will return common element

for x in dinner_table:
    print(x)

'''

'''Dictionary
#Dictionary = a changable, unordered collection of unique key:value pairs, fast because they use hashing, allow us to access a value quickly

capitals = {'USA' : 'DC', 'india':'delhi', 'germany':'berlin'}
print(capitals['USA'])

capitals.update({'france':'paris'})
capitals.update({'USA':'Vegas'})
capitals.pop('germany')

#print(capitals.get['germany'])
print(capitals.keys())
print(capitals.values())
print(capitals.items())

'''

'''index operator
#index operator [] = gives access to a sequence's elemnt (str,list,tuples)

name = "Deepak raj!"

if (name[0].islower()):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[6:-1].upper()
last_char = name[-1]
print(first_name,last_name,last_char)

'''

'''Function
#Function = a block of code which is executed only when it is called

def hello(first_name,last_name,age):
    print ("Hello! "+first_name+" "+last_name)
    print ("You are "+str(age)+" years old")
    print ("Have a nice day")

hello("Deepakraj","Teekaraman","21") #info that are being sent to function are arguments needs matching number of parameters
'''

'''Return_statement
#Return_statement = functions send python values/object back to the caller
#                   These values/objects are known as the function's return value

def multiply(num1,num2):
    return num1*num2

x = multiply(6,8)
print(x)
'''

'''Keyword arguments
#Keyword arguments = Arguments preceded by an identifier when we pass them to a funtion
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    python knows the names of the arguments that out funtion recieves

def hello(first,middle,last):
    print("Hello "+first+middle+" "+last)

hello(middle="raj",last="Teekaraman",first="deepak")
'''

'''Nested_funtion_calls
#Nested_funtion_calls = func calls inside other func calls
#                       innermost func calls are resolved first
#                        returned values is used as argument for the next outer function

num = input("Enter a whole postive number: ")
num = float(num)
num = abs(num)
num = round(num)
print (num)

num = round(abs(float(input("Enter a number: "))))
print (num)
'''

'''Scope
#Scope = The region that a variable is recognized
#        A variable is only available from inside the region it is created
#        A global locally scoped versions of a variable can be created
#        Follows L=Local, E= Enclosing, G=Global, B= built in

name = "Raj" #global scope (available inside and outside of function)

def display_name():
    name = "Deepak" #local scope(available only inside this funtion)
    print(name)

display_name()
print(name)
'''

'''Args
#Args = parameter that will pack all arguments into a tuple
#       useful so that a function can be accept a varying amount of arguments

def add(*sum_values):
    sum = 0
    sum_values = list(sum_values) #casted tuple to list to change the values
    sum_values[0] = 15
    for i in sum_values:
        sum +=i
    return sum

print (add(1,2,3,4,5))
'''

'''*kwargs
#*kwargs = parameter that will pack all arguments into a dictionary
#          useful so that a function can accept a varying amount of keywords

def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print (value,end=" ")

hello (title="Mr.",first = "Deepak",middle="raj",last="Teekaraman")
'''

'''str.format()
#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

name = "Deepak"

print("hello, my name is {}".format(name))
print("hello, my name is {:10}. Nice to meet you".format(name))
print("hello, my name is {:>10}. Nice to meet you".format(name))
print("hello, my name is {:<10}. Nice to meet you".format(name))
print("hello, my name is {:^10}. Nice to meet you".format(name))

text = "The {} jumped over the {}"
print (text.format(animal,item))

number = 3.141594
print ("The number pi is {:.2f}".format(number))
print ("The number pi is {:,}".format(number))
print ("The number pi is {:b}".format(number))
print ("The number pi is {:o}".format(number))
print ("The number pi is {:X}".format(number))
print ("The number pi is {:E}".format(number))

#print ("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow","moon"))
print("The {0} jumped over the {1}".format("cow","moon")) #positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword arguemnt
'''

'''Random variable
import random #pseudo-random

x = random.randint(1,6)
y = random.random()

mylist = ['rock','paper','scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
cards = random.shuffle(cards)

print(cards)

print(x)
print(y)
print(z)
'''

>>>>>>> 4c469c7f655bf2312451a1bfb1c7133ff4a20247
