num = int(input("Enter a number: "))
sum = 0 #sum = 1 (Sir)
for i in range(1, num): #(2, num)
  if(num % i == 0):
    sum = sum + i
if(sum == num):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")