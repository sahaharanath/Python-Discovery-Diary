# P09-type_casting.py
# Demonstrates type casting in Python, including implicit and explicit conversions.

# Example 1: Adding integers
a = 100
b = 200
print("a + b:", a + b)  # Outputs: 300

# Example 2: Adding strings
a = "100"
b = "200"
print("a + b:", a + b)
# Here, we concatenate strings instead of adding numbers because the variables are strings.

# Example 3: Concatenating strings
name1 = "Harry"
name2 = "David"
print("name1 + name2:", name1 + name2)  # Outputs: HarryDavid

# Type casting is of 2 types: Implicit and Explicit

# Implicit Type Casting
# Example 4: Adding two strings after converting them to integers
x = '2'
y = '5'
print(int(x), "+",int(y),":", int(x) + int(y))  # Outputs: 7
# Python implicitly converts string to int during the addition.

# Explicit Type Casting
# Example 5: Adding a float and an integer after explicitly converting the integer to float
c = 1.9
d = 5
print(d,"+",c,":", float(d) + c)
# Python explicitly converts the integer 'd' to float before addition.
# This is done to prevent potential data loss, providing more precision in the result.

