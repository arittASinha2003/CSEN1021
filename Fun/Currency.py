print("\t\t\t\tWelcome to CURRENCY CONVERTER")
print("\t\t\t\t-----------------------------")
print("\n")

print("1. USD to INR")
print("2. INR to USD")

print("3. DIRHAM to INR")
print("4. INR to DIRHAM")

print("5. YEN to INR")
print("6. INR to YEN")

print("7. EURO to INR")
print("8. INR to EURO")

print("9. POUND STERLING to INR")
print("10. INR to POUND STERLING")
print("\n")

choice = int(input("Enter your choice: "))

if choice == 1:
  USD = float(input("Enter value in USD: "))
  INR = USD * 77.33
  print("Converted Currency in INR: ", INR)

elif choice == 2:
  INR = float(input("Enter value in INR: "))
  USD = INR * 0.013
  print("Converted Currency in USD: ", USD)

elif choice == 3:
  DIRHAM = float(input("Enter value in DIRHAM: "))
  INR = DIRHAM * 21.05
  print("Converted Currency in INR: ", INR)

elif choice == 4:
  INR = float(input("Enter value in INR: "))
  DIRHAM = INR * 0.048
  print("Converted Currency in DIRHAM: ", DIRHAM)

elif choice == 5:
  YEN = float(input("Enter value in YEN: "))
  INR = YEN * 0.59
  print("Converted Currency in INR: ", INR)

elif choice == 6:
  INR = float(input("Enter value in INR: "))
  YEN = INR * 1.69
  print("Converted Currency in YEN: ", YEN)

elif choice == 7:
  EURO = float(input("Enter value in EURO: "))
  INR = EURO * 81.32
  print("Converted Currency in INR: ", INR)

elif choice == 8:
  INR = float(input("Enter value in INR: "))
  EURO = INR * 0.012
  print("Converted Currency in EURO: ", EURO)

elif choice == 9:
  POUND = float(input("Enter value in POUND: "))
  INR = POUND * 95.01
  print("Converted Currency in INR: ", INR)

elif choice == 10:
  INR = float(input("Enter value in INR: "))
  POUND = INR * 0.011
  print("Converted Currency in POUND: ", POUND)

else:
  print("Invalid Choice!!!")