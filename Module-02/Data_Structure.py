L1 = [1, 1.5, 'Hello']
print(type(L1))
print(L1[1])
for i in L1:
  print(i, end = " ")

#append
L2 = []
L2.append(15)
L2.append(17)
print("\n")
print(L2)

#insert
L2.insert(1, 13)
print(L2)

#extend
L3 = [1, 1.5, 'Hi']
#L4 = [1, 1.5, 'Hello']
L2.extend(L3)
#L2.extend(L4)
print(L2)

#remove
L2.remove(13)
print(L2)

#pop
L2.pop()
print(L2)