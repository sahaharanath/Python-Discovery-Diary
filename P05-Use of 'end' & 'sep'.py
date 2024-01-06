# P05-P05-Use of 'END' & 'SEP'.py
# In a university, it is a format to store students' details: NAME ID ROLL
print("Harry", 56845, "505")

# Now, for a specific purpose, store students' details in the format: NAME-ID-ROLL, e.g.: DAVID-5896-25
print("Here we use 'sep' function")
print("HARRY", 56845, 505, sep="-")  # Using a hyphen (-)

# Using underscore (_) as a separator
print("SMITH", 85296, 205, sep="_")

# If we want to add a TAG at the end of all IDs to make it DONE, then here we use 'end'
# Suppose we will use (000OKAY) as a checkmark
print("SMITH", 85296, 205, sep="_", end=" (000OKAY) ")
print("Harry", 56845, "505")

#While using 'end' does not provide new line automatically
print("NAME", 6545, 20205, sep="_", end=" (000OKAY) ")
print("GOOD MORNING!")
#i.e. : it will give output : NAME_6545_20205 (000OKAY) GOOD MORNING!
