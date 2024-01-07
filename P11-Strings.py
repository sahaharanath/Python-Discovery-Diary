# P11-Strings.py
# Demonstrates basic string operations in Python.

# Example 1: Printing the full string
name = "Harry"
print("Full string:", name)

# Example 2: Accessing individual characters in the string
print("Character at index 0:", name[0])
print("Character at index 1:", name[1])
print("Character at index 2:", name[2])
print("Character at index 3:", name[3])
print("Character at index 4:", name[4])
# Uncommenting the line below would result in an IndexError
# print("Character at index 5:", name[5])

# To store multiline strings, we can use '''...''' or """..."""
# Example 3: Using ''' for a multiline string
passage1 = '''Harry is a good boy.
He was born in Kolkata.
Now he is an engineer.'''
print(passage1)

# Example 4: Using """ for a multiline string
passage2 = """Harry is a good boy.
He was born in Kolkata.
Now he is an engineer."""
print(passage2)
