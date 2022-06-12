## Only reads from file
f = open('document.txt', 'r')
print(f.read())

## Deletes existing text and adds new text in file. If file not exists, it creates new one
# f = open('document.txt', 'w')
# f.write('Hi')

## Adds upon existing file. If file not exists, it creates new one
# f = open('document.txt', 'a')
# f.write('. Welcome')

f.close()