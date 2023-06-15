# 1	r	It opens the file to read-only mode. The file pointer exists at the beginning. The file is by default open in this mode if no access mode is passed.

# 2	rb	It opens the file to read-only in binary format. The file pointer exists at the beginning of the file.

# 3	r+	It opens the file to read and write both. The file pointer exists at the beginning of the file.

# 4	rb+	It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.

# 5	w	It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name. The file pointer exists at the beginning of the file.

# 6	wb	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists. The file pointer exists at the beginning of the file.

# 7	w+	It opens the file to write and read both. It is different from r+ in the sense that it overwrites the previous file if one exists whereas r+ doesn't overwrite the previously written file. It creates a new file if no file exists. The file pointer exists at the beginning of the file.

# 8	wb+	It opens the file to write and read both in binary format. The file pointer exists at the beginning of the file.

# 9	a	It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. It creates a new file if no file exists with the same name.

# 10	ab	It opens the file in the append mode in binary format. The pointer exists at the end of the previously written file. It creates a new file in binary format if no file exists with the same name.

# 11	a+	It opens a file to append and read both. The file pointer remains at the end of the file if a file exists. It creates a new file if no file exists with the same name.

# 12	ab+	It opens a file to append and read both in binary format. The file pointer remains at the end of the file.


# f = open("file.txt","r")    
    
# if f:    
#     print("file is opened successfully")   

# with open("file.txt",'r') as f:    
#     content = f.read();    
#     print(content)    



# file= open("file.txt", "w")  
  
# file.write('''''Python is the modern day language. It makes things so simple. 
# It is the fastest-growing programing language''')  
# fr=file.read()
# print(fr)
# file.close()



#open the file.txt in write mode.    
# fileptr = open("file.txt","a")  
    
#overwriting the content of the file    
# fileptr.write(" Python has an easy syntax and user-friendly interaction.")    
# print(fileptr.read())
#closing the opened file     
# fileptr.close()  





# try:  
#    fileptr = open("file.txt")  
#    # perform file operations  
# finally:  
#    fileptr.close()  


with open("file.txt",'r') as f:    
    content = f.read();    
    print(content)    


# open()        used to open the file
# close()       close the file
# read()        to read the file
# readline()    only one line read
# readlines()   read multiple lines
# seek()        used to give postion to the curser
# tell()        it tells position of the curser






# f=open('file.txt')

# print(f'curser position -- {f.tell()}')
# print(f.read())

# print(f'curser position -- {f.tell()}')

# print('before seek method :')
# f.seek(2)
# print('after seek method')


# print(f'curser position -- {f.tell()}')
# print(f.read())
# f.close()

# f.readline()

# lines=f.readlines()
# print(len(lines))

# name                  tell us name of file
# closed                return ture or false

# print(f.name)

# f.close()

# print(f.closed)




# *****************************************************************************************888888888
# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:


f = open("file.txt", "r")
print(f.read())






# Open a file on a different location:

# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())






# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:


# Return the 5 first characters of the file:

f = open("file.txt", "r")
print(f.read(5))




# Loop through the file line by line:

f = open("file.txt", "r")
for x in f:
  print(x)