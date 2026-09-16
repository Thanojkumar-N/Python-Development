# Task 5: Palindrome Checker
# Write a Python function that checks whether a given string is a palindrome.

def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    text = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is NOT a palindrome!")
