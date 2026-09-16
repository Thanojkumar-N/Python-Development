def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Sequence:")

    for i in range(n):
        print(a, end=" ")

        # Calculate the next term
        a, b = b, a + b


# Get number of terms from user
n = int(input("Enter the number of terms: "))

# Generate Fibonacci sequence
fibonacci(n)