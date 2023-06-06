f=open('file.txt')

print(f'curser position -- {f.tell()}')
print(f.read())

print(f'curser position -- {f.tell()}')

print('before seek method :')
f.seek()
print('after seek method')


print(f'curser position -- {f.tell()}')