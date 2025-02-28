import re

# 1. Match a string that has an 'a' followed by zero or more 'b''s.
def match_ab_string(s):
    pattern = r"ab*"
    return bool(re.match(pattern, s))

input_string = input("Enter a string: ")
print(match_ab_string(input_string))

# 2. Match a string that has an 'a' followed by two to three 'b'.
def match_ab_range(s):
    pattern = r"ab{2,3}"
    return bool(re.match(pattern, s))

input_string = input("Enter a string: ")
print(match_ab_range(input_string))

# 3. Find sequences of lowercase letters joined with an underscore.
def find_lowercase_with_underscore(s):
    pattern = r"[a-z]+(?:_[a-z]+)*"
    return re.findall(pattern, s)

input_string = input("Enter a string: ")
print(find_lowercase_with_underscore(input_string))

# 4. Find sequences of one uppercase letter followed by lowercase letters.
def find_uppercase_lowercase(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)

input_string = input("Enter a string: ")
print(find_uppercase_lowercase(input_string))

# 5. Match a string that has an 'a' followed by anything, ending in 'b'.
def match_a_to_b(s):
    pattern = r"a.*b"
    return bool(re.match(pattern, s))

input_string = input("Enter a string: ")
print(match_a_to_b(input_string))

# 6. Replace all occurrences of space, comma, or dot with a colon.
def replace_space_comma_dot(s):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":", s)

input_string = input("Enter a string: ")
print(replace_space_comma_dot(input_string))

# 7. Convert snake case string to camel case string.
def snake_to_camel_case(s):
    return re.sub(r'_(.)', lambda x: x.group(1).upper(), s)

input_string = input("Enter a snake_case string: ")
print(snake_to_camel_case(input_string))

# 8. Split a string at uppercase letters.
def split_at_uppercase(s):
    return re.findall(r'[A-Z]?[a-z]+', s)

input_string = input("Enter a string: ")
print(split_at_uppercase(input_string))

# 9. Insert spaces between words starting with capital letters.
def insert_spaces_between_capitals(s):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", s)

input_string = input("Enter a string: ")
print(insert_spaces_between_capitals(input_string))

# 10. Convert a given camel case string to snake case.
def camel_to_snake_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

input_string = input("Enter a camelCase string: ")
print(camel_to_snake_case(input_string))
