#Python Classes

'''
1.Define a class which has at least two methods: getString: 
to get a string from console input printString: to print the string in upper case.
'''

class getPrint:
    def __init__ (self):
        self.input = ""

    def getString(self):
        self.input = input()

    def printString(self):
        print(self.input.upper)


'''
2.Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
'''

class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length ** 2
    
'''
3.Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
'''
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

'''
4.Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points'''
import math

class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
    def show(self):
        print(f"Point({self.x}, {self.y})")
    def move(self, x2, y2):
        self.x = x2
        self.y = y2
        print(f"Moved to new coordinates: ({self.x}, {self.y})")
    def dist(self, other_point):
        distance = math.sqrt((other_point.x-self.x)**2 + (other_point.y-self.y)**2)
    
'''
5. Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. 
Instantiate your class, make several deposits and withdrawals, 
and test to make sure the account can't be overdrawn.
'''
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
    def withdraw(self, amount):
        if amount>0 and amount <= self.balance:
            self.balance -= amount

'''
6. Write a program which can filter prime numbers in a list by using filter function. 
Note: Use lambda to define anonymous functions.
'''

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

numbers = [10, 23, 4, 11, 12, 17, 15, 18, 13, 5]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers in the list:", prime_numbers)

#Python Function1

'''
1. A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams
'''
def converter(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("enter the grams: "))
ounces = converter(grams)

print(f"{grams} grams = {ounces} ounces.")

'''
2. Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
'''

def converter(Fahrenheit):
    centigrade = (5 / 9) * (Fahrenheit - 32)
    return centigrade

Fahrenheit = float(input("enter the Fahrenheit: "))
centigrade = converter(Fahrenheit)

print(f"{Fahrenheit} Fahrenheit = {centigrade} centigrade.")

'''
3. Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? 
create function: solve(numheads, numlegs):
'''

def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads)//2
    chickens = numheads - rabbits
    return chickens, rabbits

numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)

print(f"Chickens: {chickens}, Rabbits: {rabbits}")

'''
4. You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers 
as an agrument and returns only prime numbers from the list.
'''

def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return [num for num in numbers if is_prime(num)]

numbers = [10, 23, 4, 11, 12, 17, 15, 18, 13, 5]
prime_numbers = filter_prime(numbers)
print("Prime numbers: ",prime_numbers)

#5. Write a function that accepts string from user and print all permutations of that string.

def generate_permutations(s, current_permutation=""):
    if len(s) == 0:
        print(current_permutation)
        return
    
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        generate_permutations(remaining, current_permutation + s[i])

input_string = input("Enter a string to generate permutations: ")
generate_permutations(input_string)

'''
6. Write a function that accepts string from user, return a sentence with the words reversed. 
We are ready -> ready are We
'''

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

input_sentence = input("Enter a sentence: ")
result = reverse_sentence(input_sentence)
print(result)

'''
7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))  

'''
8. Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#9. Write a function that computes the volume of a sphere given its radius.

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

radius = float(input("enter the radius: "))
volume = sphere_volume(radius)
print(volume)

'''
10. Write a Python function that takes a list and returns a new list 
with unique elements of the first list. Note: don't use collection set.
'''

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

user_input = input("Enter a list of elements (comma separated): ")
lst = [int(x) for x in user_input.split(',')]

print("Unique elements:", unique_elements(lst))

'''
11. Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

user_input = input("Enter a word or phrase: ")
print(is_palindrome(user_input))

'''
12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
'''

def histogram(lst):
    for num in lst:
        print('*' * num)

user_input = input("Enter a list of integers (comma separated): ")
lst = [int(x) for x in user_input.split(',')]

histogram(lst)

'''
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
'''

import random

def guessnum_game():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    random_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guessnum_game()

#Python Functions2

#Dictionary of movies
'''
1. Write a function that takes a single movie and returns True if its IMDB score is above 5.5

2. Write a function that returns a sublist of movies with an IMDB score above 5.5.

3. Write a function that takes a category name and returns just those movies under that category.

4. Write a function that takes a list of movies and computes the average IMDB score.

5. Write a function that takes a category and computes the average IMDB score.

'''
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#1. Function that returns True if a movie's IMDB score is above 5.5
def is_above_5_5(movie):
    return movie['imdb'] > 5.5

#2. Function that returns a sublist of movies with IMDB score above 5.5
def filter_movies_above_5_5(movies_list):
    return [movie for movie in movies_list if movie['imdb'] > 5.5]

#3. Function that takes a category and returns the movies under that category
def get_movies_by_category(movies_list, category):
    return [movie for movie in movies_list if movie['category'].lower() == category.lower()]

#4. Function that computes the average IMDB score of a list of movies
def average_imdb_score(movies_list):
    if not movies_list:
        return 0
    total_score = sum(movie['imdb'] for movie in movies_list)
    return total_score / len(movies_list)

#5. Function that computes the average IMDB score for a given category
def average_imdb_score_by_category(movies_list, category):
    category_movies = get_movies_by_category(movies_list, category)
    return average_imdb_score(category_movies)