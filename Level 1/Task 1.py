# Task 1: String Reversal
# Create a Python function that takes a string as input and returns the reversed string.

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_text = reverse_string(user_input)
    print(f"Reversed string: {reversed_text}")
