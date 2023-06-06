# open()        used to open the file
# close()       close the file
# read()        to read the file
# readline()    only one line read
# readlines()   read multiple lines
# seek()        used to give postion to the curser
# tell()        it tells position of the curser






f=open('file.txt')

print(f'curser position -- {f.tell()}')
print(f.read())

print(f'curser position -- {f.tell()}')

print('before seek method :')
f.seek(2)
print('after seek method')


print(f'curser position -- {f.tell()}')
print(f.read())
f.close()

# f.readline()
# f.readlines()