# P10-taking_input.py
# Demonstrates taking user input and handling input types in Python.

# Example 1: Taking input for name and age
name = input("What is your name? : ")
age = input("How old are you? : ")
print("My name is:", name)
print("My age is:", age)

# Example 2: Taking input for two numbers and demonstrating input type issues
x = input("Enter the first number : ")  # User input is treated as a string
y = input("Enter the second number : ")  # User input is treated as a string
print("The sum of", x, "and", y, "is:", x + y)  # Concatenates strings, not adding numbers

# To get the expected result, typecast the input to integers
print("The sum of", x, "and", y, "is:", int(x) + int(y))

# Alternatively, specify the type while taking user input
m = int(input("Enter the value of 'm' : "))
n = int(input("Enter the value of 'n' : "))
print("The sum of", m, "and", n, "is:", m + n)
