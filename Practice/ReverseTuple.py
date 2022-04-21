#Reverse the tuple
def reverse_tuple(t):
  reversed_tuple = t[::-1]
  return reversed_tuple

if __name__=='__main__':
  t=(10,30,50,60)
  print(reverse_tuple(t))
  #expected output (60,50,30,10)