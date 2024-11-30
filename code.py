# Function to calculate the factorial of a number
def factorial(n):
    # If the number is negative, return an error message
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # Base case for 0! = 1
    elif n == 0:
        return 1
    else:
        # Loop to calculate factorial for positive integers
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input from the user
num = int(input("Enter a number to find its factorial: "))

# Calculate and print the factorial
fact = factorial(num)
print(f"The factorial of {num} is: {fact}")
