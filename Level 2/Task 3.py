def check_password_strength(password):
    # Check password length
    length = len(password)

    # Check for uppercase letter
    has_upper = False

    # Check for lowercase letter
    has_lower = False

    # Check for digit
    has_digit = False

    # Check for special character
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    # Check all conditions
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    elif length >= 6 and has_upper and has_lower and has_digit:
        return "Medium Password"
    else:
        return "Weak Password"


# Get password from user
password = input("Enter your password: ")

# Check and display strength
result = check_password_strength(password)

print("Password Strength:", result)