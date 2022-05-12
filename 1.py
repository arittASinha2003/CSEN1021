def spring():
  return "It is Spring"
def summer():
  return "It is Summer"
def autumn():
  a = float(input("Value: "))
  b = str(a*1.1)
  # c = str(b)
  return "USD: "+ b
def winter():
  return "It is Winter"
def default():
  return "Invalid Season!"

switch_case = {
  1: spring,
  2: summer,
  3: autumn,
  4: winter
}

def switch(x):
  return switch_case.get(x, default)()

# print(switch(1))
num = int(input("Enter your choice: "))
print(switch(num))