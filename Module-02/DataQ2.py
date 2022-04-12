'''Program to print a specific list after removing the 0th, 4th and 5th elements.
Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output: ['Green', 'White', 'Black']'''

L1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
L2 = []
print(len(L1))
for i in range(len(L1)):
  if((i == 0) or (i==4) or (i == 5)):
    continue
  else:
    L2.append(L1[i])
print(L2)