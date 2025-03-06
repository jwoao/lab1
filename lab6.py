#Python builtin functions exercises

#Write a Python program with builtin function to multiply all the numbers in a list

from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(result)

'''Write a Python program with builtin function that accepts a string 
and calculate the number of upper case letters and lower case letters'''

def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    
    return upper_count, lower_count

input_string = input("Enter a string: ")
upper_count, lower_count = count_case(input_string)

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(string):
    return string == string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''
Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''

import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)

number = int(input("Enter a number: "))
delay_ms = int(input("Enter delay in milliseconds: "))

result = delayed_square_root(number, delay_ms)

print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

#Write a Python program with builtin function that returns True if all elements of the tuple are true.

def check_all_true(tpl):
    return all(tpl)

input_tuple = tuple(map(int, input("Enter a tuple of integers separated by spaces: ").split()))

result = check_all_true(input_tuple)

print(result)

#Python Directories and Files exercises

#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_directories_files(path):
    # List only directories
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    # List only files
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    # List all directories and files
    print("\nAll entries (directories + files):")
    for entry in os.listdir(path):
        print(entry)

path = input("Enter the path: ")
list_directories_files(path)

#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(f"Path exists: {exists}")
    print(f"Path is readable: {readable}")
    print(f"Path is writable: {writable}")
    print(f"Path is executable: {executable}")

path = input("Enter the path: ")
check_access(path)

#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

def check_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Path exists.")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("Path does not exist.")

path = input("Enter the path: ")
check_path(path)

#Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

file_path = input("Enter the file path: ")
count_lines_in_file(file_path)

#Write a Python program to write a list to a file.

def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")
    print(f"List written to {file_path}")

file_path = input("Enter the file path: ")
lst = ["apple", "banana", "cherry"]
write_list_to_file(file_path, lst)

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

def create_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")

create_files()

#Write a Python program to copy the contents of a file to another file

def copy_file(src_path, dest_path):
    try:
        with open(src_path, 'r') as src_file:
            content = src_file.read()
        
        with open(dest_path, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"Content copied from {src_path} to {dest_path}")
    except FileNotFoundError:
        print("Source file not found.")

src_path = input("Enter the source file path: ")
dest_path = input("Enter the destination file path: ")
copy_file(src_path, dest_path)

#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted.")
        else:
            print("You do not have write access to the file.")
    else:
        print("File does not exist.")

file_path = input("Enter the file path to delete: ")
delete_file(file_path)
