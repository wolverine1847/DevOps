# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a number: "))

# Ensure the number is non-negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Output the result
    print(f"The factorial of {num} is {factorial(num)}")

//tyhfgberauehfgnritjrejgperhgp5q3iuohtorhafh3o5tueraoifher
