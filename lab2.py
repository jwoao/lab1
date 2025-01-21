#Python Booleans

#Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables

#Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

#Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True

#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean

#Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

#Python Operators

print(10 + 5)

#Operator Precedence

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)

#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

#Python Lists

mylist = ["apple", "banana", "cherry"]

#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length

#Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types

#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

#What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Python - Access List Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Print the last item of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #Return the third, fourth, and fifth item:

#This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: #Check if "apple" is present in the list
  print("Yes, 'apple' is in the fruits list")

#Python - Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #Change the second item
print(thislist)

#Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #Change the second value by replacing it with TWO new values
print(thislist)

#Change the second and third value by replacing it with ONE value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items: The insert() method

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Insert "watermelon" as the third item
print(thislist)

#Python - Add List Items

#To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #Using the append() method to append an item
print(thislist)

#The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #Insert an item as the second position
print(thislist)

#Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #Add the elements of tropical to thislist
print(thislist)

#Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #Add elements of a tuple to a list
print(thislist)

#Python - Remove List Items

#Remove Specified Item: The remove() method

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Remove "banana"
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #Remove the first occurrence of "banana"
print(thislist)

#Remove Specified Index: The pop() method

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Remove the second item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #Remove the last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #Remove the first item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #Delete the entire list

#Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear() #Clear the list content
print(thislist)

#Python - Loop Lists

#Loop Through a List

#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Python - List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] #this line

print(newlist)

'''
The Syntax
newlist = [expression for item in iterable if condition == True]
'''

#Condition

newlist = [x for x in fruits if x != "apple"] #Only accept items that are not "apple"

#With no if statement:

newlist = [x for x in fruits]

#Iterable

newlist = [x for x in range(10)] #You can use the range() function to create an iterable

newlist = [x for x in range(10) if x < 5] #Accept only numbers lower than 5

#Expression

newlist = [x.upper() for x in fruits] #Set the values in the new list to upper case

newlist = ['hello' for x in fruits] #Set all values in the new list to 'hello'

newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"

#Python - Sort Lists

#Sort List Alphanumerically

#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #Sort the list descending
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #Sort the list descending
print(thislist)

#Customize Sort Function

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort

#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #Reverse the order of the list items
print(thislist)

#Python - Copy Lists

#Use the copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Use the slice Operator: using the ":" (slice) operator.

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Python - Join Lists

#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 
print(list3)

#Append list2 into list1: 

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Python Tuples

mytuple = ("apple", "banana", "cherry")

#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #Print the number of items in the tuple

#Create Tuple With One Item

thistuple = ("apple",) #One item tuple, remember the comma
print(type(thistuple))

#NOT a tuple
thistuple = ("apple") 
print(type(thistuple))

#Tuple Items - Data Types

#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

#What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor (to make a tuple)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Python - Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Print the second item in the tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #Print the last item of the tuple

#Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Return the third, fourth, and fifth item

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #Return the items from the beginning to, but NOT included, "kiwi"

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #Return the items from "cherry" and to the end

#Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #Return the items from index -4 (included) to index -1 (excluded)

#Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: #Check if "apple" is present in the tuple
  print("Yes, 'apple' is in the fruits tuple")

#Python - Update Tuples

#Change Tuple Values

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items

#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",) #Create a new tuple with the value "orange"
thistuple += y #Add that tuple
 
print(thistuple)

#Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) #Convert the tuple into a list
y.remove("apple") #Remove "apple"
thistuple = tuple(y) #Convert it back into a tuple

'''
thistuple = ("apple", "banana", "cherry")
del thistuple #The del keyword can delete the tuple completely:
print(thistuple) #this will raise an error because the tuple no longer exists
'''

#Python - Unpack Tuples

#Unpacking a Tuple

#Packing a tuple:

fruits = ("apple", "banana", "cherry")

#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk *

#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Python - Loop Tuples

#Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple: #Iterate through the items
  print(x) #Print the values

#Loop Through the Index Numbers

#Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Using a While Loop

#Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Python - Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2 #Join two tuples
print(tuple3)

#Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #Multiply the fruits tuple by 2

print(mytuple)

#Python Sets

myset = {"apple", "banana", "cherry"}

#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Get the Length of a Set

thisset = {"apple", "banana", "cherry"}

print(len(thisset)) #Get the number of items in a set

#Set Items - Data Types

#String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"} #A set with strings, integers and boolean values

#What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

#Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Python - Access Set Items

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Python - Add Set Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #Add an item to a set, using the add() method

print(thisset)

#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #Remove "banana" by using the remove() method:

print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #Remove "banana" by using the discard() method

print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #Remove a random item by using the pop() method

print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear() #The clear() method empties the set

print(thisset)
'''
thisset = {"apple", "banana", "cherry"}
del thisset #The del keyword will delete the set completely

print(thisset)
'''
#Python - Loop Sets

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Python - Join Sets

#Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #Join set1 and set2 into a new set
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #Use | to join two sets
print(set3)

#Join Multiple Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) #Join multiple sets with the union() method
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4 #Use | to join two sets
print(myset)

#Join a Set and a Tuple

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Update

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2) #The update() method inserts the items in set2 into set1
print(set1)

#Intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2) #Join set1 and set2, but keep only the duplicates
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2 #Use & to join two sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2) #Keep the items that exist in both set1, and set2

print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2) #Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates

print(set3)

#Difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #Keep all items from set1 that are not in set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 #Use - to join two sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2) #Use the difference_update() method to keep the items that are not present in both sets
print(set1)

#Symmetric Differences

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #Keep the items that are not present in both sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 #Use ^ to join two sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2) #Use the symmetric_difference_update() method to keep the items that are not present in both sets
print(set1)

#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed

#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length

print(len(thisdict)) #Print the number of items in the dictionary

#Dictionary Items - Data Types

#String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#The dict() Constructor
 
thisdict = dict(name = "John", age = 36, country = "Norway") #Using the dict() method to make a dictionary
print(thisdict)

#Python - Access Dictionary Items

#Accessing Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] #Get the value of the "model" key

x = thisdict.get("model") #Get the value of the "model" key using get() method

#Get Keys

x = thisdict.keys() #Get a list of the keys

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values

x = thisdict.values() #Get a list of the values

#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#Get Items

x = thisdict.items() #Get a list of the key:value pairs

#Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#Check if Key Exists

#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Python - Change Dictionary Items

#Change Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #Change the "year" to 2018

#Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) #Update the "year" of the car by using the update() method

#Python - Add Dictionary Items

#Adding Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) #Add a color item to the dictionary by using the update() method

#Python - Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #The pop() method removes the item with the specified key name
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] #The del keyword removes the item with the specified key name
print(thisdict)

'''
The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #The clear() method empties the dictionary
print(thisdict)

#Python - Loop Dictionaries

#Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values(): #Use the values() method to return values of a dictionary
  print(x)

for x in thisdict.keys(): #Use the keys() method to return the keys of a dictionary
  print(x)

for x, y in thisdict.items(): #Loop through both keys and values, by using the items() method
  print(x, y)

#Python - Copy Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #Make a copy of a dictionary with the copy() method
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #Make a copy of a dictionary with the dict() function
print(mydict)

#Python - Nested Dictionaries

#Nested Dictionaries

#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access Items in Nested Dictionaries

print(myfamily["child2"]["name"]) #Print the name of child 2

#Loop Through Nested Dictionaries

#Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


#Python If ... Else

#If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")

#Indentation

'''
If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
'''

#Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If

if a > b: print("a is greater than b") #One line if statement

#Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B") #One line if else statement

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #One line if else statement, with 3 conditions

#And

a = 200
b = 33
c = 500
if a > b and c > a: #Test if a is greater than b, AND if c is greater than a
  print("Both conditions are True")

#Or

a = 200
b = 33
c = 500
if a > b or a > c: #Test if a is greater than b, OR if a is greater than c
  print("At least one of the conditions is True")

#Not

a = 33
b = 200
if not a > b: #Test if a is NOT greater than b
  print("a is NOT greater than b")

#Nested If

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
'''if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.'''
a = 33
b = 200

if b > a:
  pass

#Python While Loops

#Print i as long as i is less than 6:

i = 1
while i < 6: 
  print(i)
  i += 1

#The break Statement

#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:  
    break
  i += 1

#The continue Statement

#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue 
  print(i)

#The else Statement

#Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else: 
  print("i is no longer less than 6")

#Python For Loops

#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String

#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

#The break Statement

#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement

#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function

#Using the range() function:

for x in range(6):
  print(x)

#Using the start parameter:

for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#Else in For Loop

#Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops

#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement
'''
for loops cannot be empty, but if you for some reason have a for loop with no content,
put in the pass statement to avoid getting an error.
'''

for x in [0, 1, 2]:
  pass