import math

# Ceil, Floor, Fabs Functions
num = float(input("Enter a decimal number: "))
print("Floor Value:", math.floor(num))
print("Ceil Value:", math.ceil(num))
print("Absolute Value:", math.fabs(num))
print("\n")

# Pow Function
base = int(input("Enter base value: "))
power = int(input("Enter power value: "))
print("Power Value:", math.pow(base, power))
print("\n")

# Sqrt Function
num1 = int(input("Enter a number: "))
print("Square Root:", math.sqrt(num1))
print("\n")

# Trunc Function
num2 = float(input("Enter a decimal number: "))
print("Trunc Value:", math.trunc(num2))
print("\n")

# Fmod Function
num3 = int(input("Enter dividend: "))
num4 = int(input("Enter divisor: "))
print("Remainder Value:", math.fmod(num3, num4))
print("\n")

# PI Function
print("PI Value:", math.pi)
print("\n")