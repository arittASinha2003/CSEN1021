#Swap two tuples in Python
def swap_tuple(t1,t2):
  temp_tuple = t1
  t1 = t2
  t2 = temp_tuple
  return tuple((t1, t2))

if __name__=='__main__':
  tuple1 = (11, 22)
  tuple2 = (99, 88)
  print(swap_tuple(tuple1,tuple2))
  #expected output 
 # tuple1: (99, 88)
 # tuple2: (11, 22)