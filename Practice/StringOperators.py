char = input("Enter a string: ")
print("Capitalize: ", char.capitalize())
print("Upper: ", char.upper())
print("Lower: ", char.lower())
print("Title: ", char.title())
print("Casefold: ", char.casefold())
print("Center: ", char.center(50))
print("\n")

print("Isalnum: ", char.isalnum())
print("Isalpha: ", char.isalpha())
print("Isascii: ", char.isascii())
print("Isdecimal: ", char.isdecimal())
print("Isdigit: ", char.isdigit())
print("Isidentifier: ", char.isidentifier())
print("Islower: ", char.islower())
print("Isnumeric: ", char.isnumeric())
print("Isprintable: ", char.isprintable())
print("Isspace: ", char.isspace())
print("Istitle: ", char.istitle())
print("Isupper: ", char.isupper())
print("Join: ", "||".join(char))
print("Split: ", char.split())
print("\n")

word = input("Enter word to count and find: ")
print("Count: ", char.count(word))
print("Find: ", char.find(word))