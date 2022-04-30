## Creating QR Code

# import qrcode
# qr_data = input("Enter the data: ")
# img = qrcode.make(qr_data)  # ("India")
# file_name = input("Enter file name: ")
# img.save(file_name)  # ("QRCode.jpg")

## Decoding QR Code

# import cv2
# d = cv2.QRCodeDetector()
# file_name = input("Enter file name: ")
# val, _, _ = d.detectAndDecode(cv2.imread(file_name))
# print(val)

def createQR():
  import qrcode
  qr_data = input("Enter the data: ")
  img = qrcode.make(qr_data)  # ("India")
  file_name = input("Enter file name: ")
  img.save(file_name)  # ("QRCode.jpg")

def decodeQR():
  import cv2
  d = cv2.QRCodeDetector()
  file_name = input("Enter file name: ")
  val, _, _ = d.detectAndDecode(cv2.imread(file_name))
  print(val)

print("Enter your choice:")
print("1. Creating QR Code")
print("2. Decoding QR Code")
print("\n")
choice = int(input("Choice: "))

if choice == 1:
  createQR()
elif choice == 2:
  decodeQR()
else:
  print("Invalid Choice!!")