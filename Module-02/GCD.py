def gcd(x, y):
  if x > y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
      gcd = i
  return gcd
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n")
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))