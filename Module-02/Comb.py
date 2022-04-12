def combination(n, r):
  if (n < r) or (n == r):
    return 1
  else:
    fact = 1
    temp = n
    while (temp > 1):
      fact = fact * temp
      temp = temp - 1
    num = fact
    temp1 = n - r
    fact = 1
    while (temp1 > 1):
      fact = fact * temp1
      temp1 = temp1 - 1
    den1 = fact
    temp2 = r
    