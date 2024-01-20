# P18-itwise Operators.py
# Demonstrates bitwise operators in Python.

# Example 1: Using 'bin' function to find the binary value of a number
value = 100
bin_value = bin(value)
print("The binary representation of", value, "is:", bin_value)

# Example 2: '&' (Bitwise AND) Operator
x = 10
y = 8
print("'&' Operator")
result_and = x & y
print(x, "&", y, "is", result_and)

# Example 3: '|' (Bitwise OR) Operator
print("'|' Operator")
result_or = x | y
print(x, "|", y, "is", result_or)

# Example 4: '^' (Bitwise XOR) Operator
print("'^' Operator")
result_xor = x ^ y
print(x, "^", y, "is", result_xor)
