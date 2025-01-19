print("Hello, World!")

#Python Version:

import sys
print(sys.version)


#Python Indentation:

if 5 > 2:
  print("Five is greater than two!")


'''
Syntax Error:
 skip the indentation
if 5 > 2:
print("Five is greater than two!")
'''

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

'''
Syntax Error:
You have to use the same number of spaces in the same block of code
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
'''

#Variables in Python:

x = 5
y = "Hello, World!"

#Comments:

#This is a comment.
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in
#more than just one line
print("Hello, World!")

#better to write:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#Variables:

#Creating variables:

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the Type:

x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''
Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
'''

#Multi Words Variable Names:

    #Camel Case: Each word, except the first, starts with a capital letter:
myVariableName = "John"

    #Pascal Case: Each word starts with a capital letter:
MyVariableName = "John"

    #Snake Case: Each word is separated by an underscore character:
my_variable_name = "John"

#Many Values to Multiple Variables:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables:
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#also + can be used
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#+ as math operator
x = 5
y = 10
print(x + y)

'''
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

Example
x = 5
y = "John"
print(x + y)
'''

x = 5
y = "John"
print(x, y)

#Global Variables:

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

'''
To change the value of a global variable inside a function, 
refer to the variable by using the global keyword:
'''

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Getting the Data Type:

x = 5
print(type(x))

#Setting the Data Type:

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType	

#Setting the Specific Data Type:

x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	

#Python Numbers:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#To verify the type of any object in Python, use the type() function:

print(type(x))
print(type(y))
print(type(z))

#Int:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex("j" as the imaginary part):

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number:

import random

print(random.randrange(1, 10))

#Specify a Variable Type:

#Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Python Strings:

#'hello' is the same as "hello":

print("Hello")
print('Hello')

#Quotes Inside Quotes:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable:

a = "Hello"
print(a)

#Multiline Strings:

    #You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

    #Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays:

a = "Hello, World!"
print(a[1])

#Looping Through a String:

for x in "banana":
  print(x)

#String Length:

#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

#Check String:

#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT:

#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Slicing Strings:

#Slicing:

#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Slice From the Start:

#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

#Slice To the End:

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#Negative Indexing:

'''
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])

#Modify Strings:

#Upper Case:

a = "Hello, World!"
print(a.upper())

#Lower Case:

a = "Hello, World!"
print(a.lower())

#Remove Whitespace:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String:

a = "Hello, World!"
print(a.replace("H", "J"))

#Split String:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation:

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format:

#we cannot combine strings and numbers like this:

'''
age = 36
txt = "My name is John, I am " + age
print(txt)
'''

#F-Strings:

#Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers:

#Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape Character:
'''
You will get an error if you use double quotes inside 
a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."
'''

#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."