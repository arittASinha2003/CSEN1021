lower=int(input("Enter the lower limit for the range: "))
upper=int(input("Enter the upper limit for the range: "))
for i in range(lower,upper+1):
  if(i%2!=0):
    print(i)
for j in range(lower, upper+1):
  if (j % 2 == 0):
    print("Even Numbers:")
    print(j)