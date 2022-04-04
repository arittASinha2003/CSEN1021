p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter number of years: "))

ci = p * (pow((1 + r / 100), t))

print("\n")

print("Compound Interest: ", ci)