with open("currencyData.txt") as f:
  lines = f.readlines()

currencyDict = {}
for line in lines:
  parsed = line.split("\t")
  currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount in INR: "))
print("\nEnter name of currency you want to convert to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("\nEnter one of the currency name: ")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
# Source: https://www.x-rates.com/table/?from=INR&amount=1