#Counts the number of occurrences of item  from a tuple
def occurences_tuple(t,a):
  count = 0
  for i in range(len(t)):
    if t[i] == a:
      count += 1
  return count

if __name__=='__main__':
  tuple1 = (50, 10, 60, 70, 50)
  a=int(input("occurence check number"))
  print(occurences_tuple(tuple1,a))
  #expected output 
 # a: 50
 # output:2