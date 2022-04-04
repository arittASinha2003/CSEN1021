"""def sum():
  print("Default Function")
sum()

if __name__=='__main__':
  sum()"""

def mult(x, y = 10, z = 12):
  multiply = x * y * z
  #print("The product of {a} * {b} * {c} is {d}".format(a = x, b = y, c = z, d = multiply)) #1
  return multiply #2
  #return #It returns None

if __name__=='__main__':
  #mult(x = 6, y = 5, z = 10) #1 #It overwrites the existing values
  #mult(10) #1 #It takes the existing values
  print("The product is:", mult(2, 10, 12)) #2