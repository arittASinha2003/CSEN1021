person1 = {"Name" : "Aritt", "Age" : 18}

print(person1)
print(person1["Age"])
print(person1["Name"])
# print(person1["Hobbies"])

print("\n")
person1["Name"] = "AS"  # Changes previous value
print(person1)

print("\n")
person1["Hobbies"] = ["Dancing", "Fishing"]  # Adds new key values
print(person1)

print("\n")
print(person1.pop("Name"))  # Displays Name
print(person1)  # Removes Name

print("\n")
for key in person1:
  print(key)
  print(person1[key])