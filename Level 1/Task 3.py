# Task 3: Email Validator
# Develop a Python function that validates whether a given string is a valid email address.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    email_input = input("Enter an email address to validate: ")
    if is_valid_email(email_input):
        print("Valid email address!")
    else:
        print("Invalid email address!")
