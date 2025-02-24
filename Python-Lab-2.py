#! /usr/bin/python3
import re

# Simple Calculator 
def simple_calculator(operation, num1, num2):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            return num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"

        case _:
            return "Error: Unsupported operation"

op = "add"
x, y = 10, 5
print(f"Result: {simple_calculator(op, x, y)}")
# ============================================================================
# Remove even numbers from a list and count the remaining ones

def filter_odds(num_list):
    odds = [n for n in num_list if n % 2 != 0]
    return odds, len(odds)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered, count = filter_odds(nums)
print(f"Odd numbers: {filtered}\nCount: {count}")


# ============================================================================
#Validate a password based on specific criteria

def validate_password(password):
    if len(password) < 8:
        return "Error: Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Error: Password must include at least one uppercase letter."
    if not re.search(r"\d", password):
        return "Error: Password must contain at least one digit."
    return "Password is strong!"

pwd = input("Enter a password: ")
print(validate_password(pwd))


# ============================================================================
# Merge multiple dictionaries into one

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

combined_dict = {**dict1, **dict2, **dict3}
print(combined_dict)

# ============================================================================
# Find the longest substring in alphabetical order

def longest_alpha_substring(text):
    max_substr = curr_substr = text[0]
    for i in range(1, len(text)):
        if text[i] >= text[i - 1]:
            curr_substr += text[i]
            if len(curr_substr) > len(max_substr):
                max_substr = curr_substr
        else:
            curr_substr = text[i]
    return max_substr

word = "abdulrahman"
print("Longest alphabetical substring:", longest_alpha_substring(word))


# ============================================================================
#  Email format validation

def check_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return "Valid Email" if re.match(pattern, email) else "Invalid Email"

sample_email = "hossam@gmail.com"
print(check_email(sample_email))

