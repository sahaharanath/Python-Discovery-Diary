# P12-memory_addresses.py
# Demonstrates memory addresses in Python.

# Example 1: Same values, same memory address
a = 10
b = 10
print("Memory address of 'a':", id(a))
print("Memory address of 'b':", id(b))

# Example 2: Different values, different memory addresses
c = 12
d = 15
print("Memory address of 'c':", id(c))
print("Memory address of 'd':", id(d))
