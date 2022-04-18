#Interchange First and Last Element of a List
def list_interchange(L1):
  size = len(L1)

  temp = L1[0]
  L1[0] = L1[size - 1]
  L1[size - 1] = temp

  return L1

if __name__=='__main__':
  L2=[12,13,17,19]
  print(list_interchange(L2))