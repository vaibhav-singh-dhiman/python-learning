# ============================================================
# STRINGS IN PYTHON
# ============================================================

# Creating a string variable
str = "python"
print(str)

# String concatenation
print(str + "New")

# Creating another string variable
str2 = "Language"

# Printing multiple strings
print(str, str2)

# Concatenating two strings
print(str + str2)

# Repeating a string multiple times
print(str * 5)

# Accessing a character using indexing
print(str[0])

# Strings are immutable, so we create a new string
# by combining a new character with a slice
str = "s" + str[1:]
print(str)


# ============================================================
# STRING SLICING
# ============================================================

str = "This is a string"

# Extract characters from index 0 to 7
print(str[0:8])

# Extract every second character from index 1 to 9
print(str[1:10:2])

# Reverse the string using slicing
print(str[::-1])
