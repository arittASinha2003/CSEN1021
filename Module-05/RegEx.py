import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

#Find all lower case characters alphabetically between "a" and "m":
print("\n")
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

#Find all digit characters:
print("\n")
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
print("\n")
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)

#Check if the string starts with 'hello':
print("\n")
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#