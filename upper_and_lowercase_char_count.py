# Write a Python function that accepts a string and counts 
# the number of upper and lower case letters.

string = "Hello JordaN"

def char_case_count(char_string):

    uppercase_char_count = 0
    lowercase_char_count = 0

    for a_char in char_string:
        if a_char.isupper():
            uppercase_char_count += 1
        elif a_char.islower():
            lowercase_char_count += 1

    # return tuple of both variables
    return (uppercase_char_count, lowercase_char_count)

count = char_case_count(string)
# Access and print tuple value with bracket notation
print(f'Uppercase count is {count[0]}') # 'Uppercase count is 3'
print(f'Lowercase count is {count[1]}') # 'Lowercase count is 8''