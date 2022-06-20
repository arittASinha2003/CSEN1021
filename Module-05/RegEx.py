# https://www.w3schools.com/python/python_regex.asp

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# Find all lower case characters alphabetically between "a" and "m":
print("\n")
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

# Find all digit characters:
print("\n")
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)

# Check if the string starts with 'hello':
print("\n")
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# Check if the string ends with 'planet':
print("\n")
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

# Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)

# Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)

# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)

# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)

# Check if the string contains either "falls" or "stays":
print("\n")
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# 