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