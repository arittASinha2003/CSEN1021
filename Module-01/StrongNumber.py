num = int(input("Enter a number: "))
sum = 0
temp = num
while (num):
  i = 1
  fact = 1
  r = num % 10
  while (i <= r):
    fact = fact * i
    i = i + 1
  sum = sum + fact
  num = num // 10
if (sum == temp):
  print("The number is a strong number")
else:
  print("The number is not a strong number")

"""Sir:
num = int(input("Enter a number: "))
c = num
fact1 = 0
while c > 0:
  fact = 1
  c1 = c % 10
  if ((c1 == 0) or (c1 == 1)):
    print(1)
  else:
    while (c1 > 1):
      fact = c1 * fact
      c1 -= 1
  fact1 = fact1 + fact
  c = c // 10
if fact1 == num:
  print("The number {0} is a strong number".format(num))
else:
  print("The number {0} is not a strong number".format(num))"""