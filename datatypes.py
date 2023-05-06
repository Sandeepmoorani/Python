print("Hello world")
x=2
y="Sandeep"
print(type(x))
print(type(y))


x=" Sandeep Moorani"
print("hello!"+x)



x=5 
y=4
z=x+y
print(x+y)
print(10+20)


# strings
x='Hello'
y="Hello"

x="""hello iam a software emgineer and iam learning first time programming language """
print(x)


# Numbers

x=1
y=1.1
z=-3
print(type(x))
print(type(y))
print(type(z))


# Tuples   
#  lists 
# lists are almost same but in lists we write variable value in Square brackets [] but in tuples round brackets ()

# tuples are used to store multiple items in a single variable 



mytup=("HI","Its","Me")
print(mytup)


lists=["abc","xyz","srt"]
print(lists)

# Dictionary
 
# Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dict={"Lachman":"Singh","Sandeep":"Moorani","Naresh":"Netani"}
print(dict)


# sets

# A set is a collection which is unordered, unchangeable*, and unindexed. 
# * Note: Set items are unchangeable, but you can remove items and add new items. 
# Sets are written with curly brackets. 

sets={1,2,34,5,2}
print(sets)


# ******************************************


# None:
# None is used to define a null value. When we assign a None value to a variable, we are essentially resetting it to its original empty state which is not the same as zero, an empty string or a False value.

# Example:

state = None
print(type(state))
# *********************************

# Binary data: bytes, bytearray, memoryview
# bytes: bytes() function is used to convert objects into byte objects, or create empty bytes object of the specified size.

# Example:

#Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1, 'utf-8')
print(arr1)
arr2 = bytes(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytes(4)
print(bytestr)