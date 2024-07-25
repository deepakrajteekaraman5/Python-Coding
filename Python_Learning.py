'''
#Hello world
print ('Hello world!')

'''

'''
#Variable is a container for value. Behave as a value that contains
first_name = "Deepakraj"
last_name = "Teekaraman"
full_name = first_name +" "+ last_name
print(type(full_name))   
print ("Hello "+full_name)
'''

'''
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
'''
#Multiple assignments in python. This will help in assigning multiple variables to one line of code at same time
name, age, height = 'deepakraj', 24, 245.55
print(name+" "+str(age)+" "+str(height))
'''

'''
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

'''
#Type casting = convert the data type of value to another data type
x = 1
y = 2.0
z = "3"

y = int(y)

print (float(x))
print (y)
print (z)
'''

'''
#user input in python
first_name = str(input("what is your first_name? "))
last_name = str (input ("what is your last_name? "))
name = first_name + last_name
age = int(input("what is your age? "))

print("Hello! "+ name + " your are  "+ str(age)+ " years old")
'''

'''
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
'''
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

'''
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
'''
#Logical operators in python (and,or,not)
temp = int(input("what is the temperature? "))

if temp >= 0 and temp <=30:
    print("the temperature is good today")
elif temp < 0 or temp >30:
    print ("It's not that good")
'''

'''
#while loop = a statement that execute it's block of code, as long as it's condition is true
name = ""
while len(name) == 0:
    name = input("enter your name: ")
print("hello! "+name)
'''

'''
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

'''
#Nested loops = the inner loop will finish all of the iterartions before finsihing one iteraton of outer loop
rows = int(input("How many rows?:"))
coulmns = int(input("how many coulmns?:"))
symbol = input("symbol")

for i in range(rows):
    for j in range(coulmns):
        print(symbol, end="") #will end and won't got to next line
  print() #to print in the next line

''' 
'''
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
'''
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

'''
#2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","briyani"]
dessert = ["cake","icecream"]

food = [drinks,dinner,dessert]

print(food[0][1])

'''

'''
#Tuples = collection which is ordered and unchangable, used to group together related data

student = ("john",21,"male")

print(student.count("john"))
print(student.index("male"))

for x in student:
    print(x)

if "john" in student:
    print("john is here")

'''

'''
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

'''
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

#index operator [] = gives access to a sequence's elemnt (str,list,tuples)

name = "Deepak raj"

if (name[0].islower()):
    name = name.capitalize()

first_name = name[0:3].upper()
print(first_name)