# Program to Find Odd Numbers From a List
def list_odd(L2):
  new_list=[]
  for i in L2:
    if i % 2 != 0:
      new_list.append(i)
  return new_list

if __name__=='__main__':
  L2=[12,13,17,19]
  print(list_odd(L2))