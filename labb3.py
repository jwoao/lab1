#Python Functions

#Creating a Function

def my_function():
  print("Hello from a function")

#Calling a Function

def my_function():
  print("Hello from a function")

my_function()

#Arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments

#This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

'''
This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
'''

#Arbitrary Arguments, *args

#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement

def myfunction():
  pass

#Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(x):
  print(x)

my_function(x = 3)

'''But when adding the , / you will get an error if you try to send a keyword argument:

def my_function(x, /):
  print(x)

my_function(x = 3)'''

#Keyword-Only Arguments

#To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

def my_function(x):
  print(x)

my_function(3)

'''
But with the *, you will get an error if you try to send a positional argument:

def my_function(*, x):
  print(x)

my_function(3)
'''

#Combine Positional-Only and Keyword-Only

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#Python Lambda

#Syntax: lambda arguments : expression

#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions?

def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #always doubles the number you send in

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3) #always triples the number you send in

print(mytripler(11))

#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Python Arrays

cars = ["Ford", "Volvo", "BMW"] #Create an array containing car names

#Access the Elements of an Array

#Get the value of the first array item:

x = cars[0]

cars[0] = "Toyota" #Modify the value of the first array item

#The Length of an Array

x = len(cars) #Return the number of elements in the cars array

#Looping Array Elements

for x in cars:
  print(x)  #Print each item in the cars array

#Adding Array Elements

cars.append("Honda") #Add one more element to the cars array

#Removing Array Elements

cars.pop(1) #Delete the second element of the cars array

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo") #Delete the element that has the value "Volvo" using the remove() method 

#Python Classes and Objects

#Create a Class

class MyClass:
  x = 5

#Create Object

p1 = MyClass()
print(p1.x)

#The __init__() Function

#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#The __str__() Function

#The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Object Methods

#nsert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self Parameter

#Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties

p1.age = 40 #Set the age of p1 to 40

#Delete Object Properties

del p1.age #Delete the age property from the p1 object

#Delete Objects

del p1 #Delete the p1 object

#The pass Statement

class Person:
  pass

#Python Inheritance

#Create a Parent Class

#Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a Child Class

#Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()

#Add the __init__() Function

class Student(Person):
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

'''To keep the inheritance of the parent's __init__() function, 
add a call to the parent's __init__() function:'''

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#Use the super() Function

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Add Properties

#Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

#Add Methods

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)