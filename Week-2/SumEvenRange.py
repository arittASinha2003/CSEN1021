""" Write a python program to print the sum of even numbers for a given range.
Example:
Input: 10
Output: 20 (2+4+6+8) """

last = int(input())
sum = 0
for i in range(0, last):
  if (i % 2 == 0):
    sum += i
print(sum)