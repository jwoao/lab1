#Python iterators and generators

#Create a generator that generates the squares of numbers up to some number N.

def square_generator():
    N = int(input("Enter the value of N: "))
    for i in range(N + 1):
        yield i ** 2

squares = square_generator()  

for square in squares:
    print(square)

'''Write a program using generator to print the even numbers between 0 and n 
in comma separated form where n is input from console.'''

def evens_generator():
    n = int(input("Enter the value of n: "))
    for i in range(n+1):
        if i%2==0:
            yield i

even_nums = evens_generator()

for evens in even_nums:
    print(evens)

'''Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.'''

def divisibility():
    n = int(input("Enter the value of n: "))
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

divisible = divisibility()

for divis in divisible:
    print(divis)

'''Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.'''

def squares():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    for i in range(a, b+1):
        yield i**2

squaree = squares()

for squa in squaree:
    print(squa)

#Implement a generator that returns all numbers from (n) down to 0.

def numbers(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter the value of n: "))
nums = numbers(n)

for num in nums:
    print(num)

#Python date

#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date after subtracting 5 days:", new_date.strftime('%Y-%m-%d'))

#Write a Python program to print yesterday, today, tomorrow.

today = datetime.now().date()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#Write a Python program to drop microseconds from datetime.

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#Write a Python program to calculate two date difference in seconds.

date1_str = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date and time (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

time_difference = date2 - date1
seconds_difference = time_difference.total_seconds()

print("The difference between the two dates in seconds:", seconds_difference)

#Python Math library

#Write a Python program to convert degree to radian.
'''
Input degree: 15
Output radian: 0.261904
'''
import math

degree = float(input("Enter the degree value: "))
radian = math.radians(degree)

print(f"{degree} degrees is equal to {radian} radians.")

#Write a Python program to calculate the area of a trapezoid.
'''
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''
height = int(input("Enter the height: "))
base1 = int(input("Enter the first value of the Base: "))
base2 = int(input("Enter the second value of the Base: "))
area = ((base1 + base2)*height)/2
print(f"The area of trapezoid is equal to {area}")

#Write a Python program to calculate the area of regular polygon.
'''
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''

def polygon_area(s, n):
    return (1/4) * n * s**2 * (1 / math.tan(math.pi / n))

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of a side: "))
area = polygon_area(length, sides)

print(f"The area of the regular polygon is: {area}")

#Write a Python program to calculate the area of a parallelogram.
'''
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
length = int(input("Enter the length of the base: "))
height = int(input("Enter the height of parallelogram: "))
area = length * height

print(f"The area of the parallelogram is {area}")

#json task

import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU'}")
print("-"*80)

for interface in data["l1PhysIf"]:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {'':<20} {speed:<10} {mtu}")
