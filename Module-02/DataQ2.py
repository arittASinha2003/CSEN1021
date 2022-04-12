'''Program to get the difference between two lists.'''

L1 = ['ECE', 'CSE', 'Mech', 'Civil']
L2 = ['EEE', 'ECE', 'CSE', 'Bio']

print("Adding 2 Lists:")
print(L1 + L2)
print("\n")

'''print("Subtracting 2 Lists:")
print(list(set(L1) - set(L2)))'''

L3 = []
for i in L1:
  #print(i)
  for j in L2:
    #print(j)
    if (j == i):
      L2.remove(j)
      #print(L2)
      #L1.remove(i)
      #print(L1)
    else:
      continue
print("Subtracting 2 Lists:")
print(L1 + L2)