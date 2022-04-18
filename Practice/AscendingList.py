#Program to check if the Given List is in Ascending Order or Not
def list_ascending(L1):
  flag = 0
  i = 1
  while i < len(L1):
    if (L1[i] < L1[i - 1]):
      flag = 1
    i += 1
  if (not flag):
    return True
  else:
    return False

if __name__=='__main__':
  L1=[12,13,17,19]
  print(list_ascending(L1))