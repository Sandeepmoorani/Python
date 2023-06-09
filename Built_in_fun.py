# Python Built-in Functions

# The Python built-in functions are defined as the functions whose functionality is pre-defined in Python.

# Python abs() Function

# The python abs() function is used to return the absolute value of a number. It takes only one argument, a number whose absolute value is to be returned. The argument can be an integer and floating-point number. If the argument is a complex number, then, abs() returns its magnitude.



#  integer number     
integer = -20  
print('Absolute value of -40 is:', abs(integer))  
  
#  floating number  
floating = -20.83  
print('Absolute value of -40.83 is:', abs(floating))  


# **************************************** all() ****************************


# The python all() function accepts an iterable object (such as list, dictionary, etc.). It returns true if all items in passed iterable are true. Otherwise, it returns False. If the iterable object is empty, the all() function returns True.


# all values true  
k = [1, 3, 4, 6]  
print(all(k))  
  
# all values false  
k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))  
  
# one true value  
k = [0, False, 5]  
print(all(k))  
  
# empty iterable  
k = []  
print(all(k))  



# *********************************** bin() ***************************


# The python bin() function is used to return the binary representation of a specified integer. A result always starts with the prefix 0b.



x =  10  
y =  bin(x)  
print (y)  


# ****************************bool()*******************************

# The python bool() converts a value to boolean(True or False) using the standard truth testing procedure.



test1 = []  
print(test1,'is',bool(test1))  
test1 = [0]  
print(test1,'is',bool(test1))  
test1 = 0.0  
print(test1,'is',bool(test1))  
test1 = None  
print(test1,'is',bool(test1))  
test1 = True  
print(test1,'is',bool(test1))  
test1 = 'Easy string'  
print(test1,'is',bool(test1))  


# ******************************** byte() ***************************


# The python bytes() in Python is used for returning a bytes object. It is an immutable version of the bytearray() function.

# It can create empty bytes object of the specified size.



string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array)  

# callable() Function  ********************************


# A python callable() function in Python is something that can be called. This built-in function checks and returns true if the object passed appears to be callable, otherwise false.



x = 8  
print(callable(x))  



# ************************************compile() Function********************

# The python compile() function takes source code as input and returns a code object which can later be executed by exec() function.


# compile string source to code  
# code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
# code = compile(code_str, 'sum.py', 'exec')  
# print(type(code))  
# exec(code)  
# exec(x)  



# ****************************exec() Function*************************


# The python exec() function is used for the dynamic execution of Python program which can either be a string or object code and it accepts large blocks of code, unlike the eval() function which only accepts a single expression.



x = 8  
exec('print(x==8)')  
exec('print(x+4)')  



# **********************************sum() Function***************************


# As the name says, python sum() function is used to get the sum of numbers of an iterable, i.e., list.



s = sum([1, 2,4 ])  
print(s)  
  
s = sum([1, 2, 4], 10)  
print(s)  



# ****************************any() Function************************


# The python any() function returns true if any item in an iterable is true. Otherwise, it returns False.


l = [4, 3, 2, 0]                              
print(any(l))                                   
  
l = [0, False]  
print(any(l))  
  
l = [0, False, 5]  
print(any(l))  
  
l = []  
print(any(l))  



# ***********************************************ascii() Function*****************


# The python ascii() function returns a string containing a printable representation of an object and escapes the non-ASCII characters in the string using \x, \u or \U escapes.



normalText = 'Python is interesting'  
print(ascii(normalText))  
  
otherText = 'Pythön is interesting'  
print(ascii(otherText))  
  
print('Pyth\xf6n is interesting')  


# ************************bytearray()***********************

# The python bytearray() returns a bytearray object and can convert objects into bytearray objects, or create an empty bytearray object of the specified size.



string = "Python is a programming language."  
  
# string with encoding 'utf-8'  
arr = bytearray(string, 'utf-8')  
print(arr)  


# *******************eval() Function******************

# The python eval() function parses the expression passed to it and runs python expression(code) within the program.



x = 8  
print(eval('x + 1'))  

# ***********************float()*******************


# The python float() function returns a floating-point number from a number or string.



# for integers  
print(float(9))  
  
# for floats  
print(float(8.19))  
  
# for string floats  
print(float("-24.27"))  
  
# for string floats with whitespaces  
print(float("     -17.19\n"))  
  
# string float error  
# print(float("xyz"))  


# *********************format() Function*****************

# The python format() function returns a formatted representation of the given value.



# d, f and b are a type  
  
# integer  
print(format(123, "d"))  
  
# float arguments  
print(format(123.4567898, "f"))  
  
# binary format  
print(format(12, "b"))  


# *************************************rozenset()*********************************

# The python frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.



# tuple of letters  
letters = ('m', 'r', 'o', 't', 's')  
  
fSet = frozenset(letters)  
print('Frozen set is:', fSet)  
print('Empty frozen set is:', frozenset())  


# ********************getattr() Function *******************************

# The python getattr() function returns the value of a named attribute of an object. If it is not found, it returns the default value.



class Details:  
    age = 22  
    name = "Phill"  
  
details = Details()  
print('The age is:', getattr(details, "age"))  
print('The age is:', details.age)  

# *****************************globals() Function****************

# The python globals() function returns the dictionary of the current global symbol table.

# A Symbol table is defined as a data structure which contains all the necessary information about the program. It includes variable names, methods, classes, etc.

age = 22  
  
globals()['age'] = 22  
print('The age is:', age)  


# ************************iter() Function****************************

# The python iter() function is used to return an iterator object. It creates an object which can be iterated one element at a time.



# list of numbers  
list = [1,2,3,4,5]  
  
listIter = iter(list)  
  
# prints '1'  
print(next(listIter))  
  
# prints '2'  
print(next(listIter))  
  
# prints '3'  
print(next(listIter))  
  
# prints '4'  
print(next(listIter))  
  
# prints '5'  
print(next(listIter))  


# ************************************locals() Function********************

# The python locals() method updates and returns the dictionary of the current local symbol table.

# A Symbol table is defined as a data structure which contains all the necessary information about the program. It includes variable names, methods, classes, etc.



def localsAbsent():  
    return locals()  
  
def localsPresent():  
    present = True  
    return locals()  
  
print('localsNotPresent:', localsAbsent())  
print('localsPresent:', localsPresent())  


# ****************************map() Function************************

# The python map() function is used to return a list of results after applying a given function to each item of an iterable(list, tuple etc.).



def calculateAddition(n):  
  return n+n  
  
numbers = (1, 2, 3, 4)  
result = map(calculateAddition, numbers)  
print(result)  
  
# converting map object to set  
numbersAddition = set(result)  
print(numbersAddition)  


# **************************memoryview() Function *******************************

# The python memoryview() function returns a memoryview object of the given argument.



#A random bytearray  
randomByteArray = bytearray('ABC', 'utf-8')  
  
mv = memoryview(randomByteArray)  
  
# access the memory view's zeroth index  
print(mv[0])  
  
# It create byte from memory view  
print(bytes(mv[0:2]))  
  
# It create list from memory view  
# print(list(mv[0:3]))  


# ********************object()****************************

# The python object() returns an empty object. It is a base for all the classes and holds the built-in properties and methods which are default for all the classes.



python = object()  
  
print(type(python))  
print(dir(python))  

# ****************************open() Function******************************

# The python open() function opens the file and returns a corresponding file object.



# opens python.text file of the current directory  
# f = open("python.txt")  
# specifying full path  
# f = open("C:/Python33/README.txt")  


# *************************# chr() Function**********************************************

# Python chr() function is used to get a string representing a character which points to a Unicode code integer. For example, chr(97) returns the string 'a'. This function takes an integer argument and throws an error if it exceeds the specified range. The standard range of the argument is from 0 to 1,114,111.



# Calling function  
result = chr(102) # It returns string representation of a char  
result2 = chr(112)  
# Displaying result  
print(result)  
print(result2)  
# Verify, is it string type?  
print("is it string type:", type(result) is str)  


# ********************************complex()********************************

# Python complex() function is used to convert numbers or string into a complex number. This method takes two optional parameters and returns a complex number. The first parameter is called a real and second as imaginary parts.



# Python complex() function example  
# Calling function  
a = complex(1) # Passing single parameter  
b = complex(1,2) # Passing both parameters  
# Displaying result  
print(a)  
print(b)  

# ****************delattr() Function*********************************
# Python delattr() function is used to delete an attribute from a class. It takes two parameters, first is an object of the class and second is an attribute which we want to delete. After deleting the attribute, it no longer available in the class and throws an error if try to call it using the class object.



class Student:  
    id = 101  
    name = "Pranshu"  
    email = "pranshu@abc.com"  
# Declaring function  
    def getinfo(self):  
        print(self.id, self.name, self.email)  
s = Student()  
s.getinfo()  
# delattr(Student,'course') # Removing attribute which is not available  
# s.getinfo() # error: throws an error  

# ***********************************
# dir() Function
# Python dir() function returns the list of names in the current local scope. If the object on which method is called has a method named __dir__(), this method will be called and must return the list of attributes. It takes a single object type argument.

# pyhton builtin functions
# Calling function  
att = dir()  
# Displaying result  
print(att)  

# ***********************************************************
# divmod() Function
# Python divmod() function is used to get remainder and quotient of two numbers. This function takes two numeric arguments and returns a tuple. Both arguments are required and numeric



# Python divmod() function example  
# Calling function  
result = divmod(10,2)  
# Displaying result  
print(result)  

# **************************************************************
# dict() Function
# Python dict() function is a constructor which creates a dictionary. Python dictionary provides three different constructors to a create dictionary.

# If no argument is passed, it creates an empty dictionary.
# If a positional argument is given, a dictionary is created with the same key-value pairs. Otherwise, pass an iterable object.
# If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument.

# dict ([**kwargs])  
# dict ([mapping, **kwargs])  
# dict ([iterable, **kwargs]) 

# Parameters
# kwargs: It is a keyword argument.

# mapping: It is another dictionary.

# iterable: It is an iterable object in the form of a key-value pair(s).



# ******************************************

# Python dict() Function Example 1
# A simple example to create an empty or non-empty dictionary. Arguments of the dictionary are optional.


# Calling function  
result = dict() # returns an empty dictionary  
result2 = dict(a=1,b=2)  
# Displaying result  
print(result)  
print(result2)  


# ***********************************

# dict() Function Example 2

# Calling function  
result = dict({'x': 5, 'y': 10}, z=20) # Creating dictionary using mapping  
result2 = dict({'x': 5, 'y': 10, 'z':20})  
# Displaying result  
print(result)  
print(result2)  

# *******************************************888

# result = dict([(1, 'One'), [2, 'Two'], [3,'Three']]) # Creating using iterable  
# result2 = dict([['x','X'],('y','Y')])  
# # Displaying result  
# print(result)  
# print(result2)  

# ***********************************************88


# filter() Function
# Python filter() function is used to get filtered elements. This function takes two arguments, first is a function and the second is iterable. The filter function returns a sequence from those elements of iterable for which function returns True.

# The first argument can be None if the function is not available and returns only elements that are True.

# function: It is a function. If set to None returns only elements that are True.

# Iterable: Any iterable sequence like list, tuple, and string.

# Return
# It returns the same as returned by the function.

# Let's see some examples of filter() function to understand it's functionality.

# Python filter() Function Example 1
# This simple example returns values higher than 5 using filter function. See the below example.

# Python filter() function example  
# def filterdata(x):  
#     if x>5:  
#         return x  
# # Calling function  
# result = filter(filterdata,(1,2,6))  
# # Displaying result  
# print(list(result))  




# filter() Function Example 2
# This function takes the first argument as a function and if no function is passed. It requires None to pass which returns all the True values. See the example below.

# Python filter() function example  
# Calling function  
# result = filter(None,(1,0,6)) # returns all non-zero values  
# result2 = filter(None,(1,0,False,True)) # returns all non-zero and True values  
# # Displaying result  
# result = list(result)  
# result2 = list(result2)  
# print(result)  
# print(result2)  



# filter() Function Example 3
# Python filter() function example  
# def mulof3(val):  
#     if val%3==0:  
#         return val  
# # Calling function  
# result = filter(mulof3,(1,3,5,6,8,9,12,14))  
# # Displaying result  
# result = list(result)  
# print(result) # multiples of 3  



# **********************************************************************

#  hash() Function
# Python has() function is used to get the hash value of an object. Python calculates the hash value by using the hash algorithm. The hash values are integers an used to compare dictionary keys during a dictionary lookup. We can hash only these types:

# Hashable types: * bool * int * long * float * string * Unicode * tuple * code object

# We cannot hash of these types:

# Non-hashable types: * bytearray * list * set * dictionary * memoryview

result = hash(21) # integer value  
result2 = hash(22.2) # decimal value  
# Displaying result  
print(result)  
print(result2)  



result = hash("javatpoint") # string value  
result2 = hash((1,2,22)) # tuple value  
# Displaying result  
print(result)  
print(result2)  


# ****************************************************************************************
# help() Function
# Python help() function is used to get help related to the object passed during the call. It takes an optional parameter and returns help information. If no argument is given, it shows the Python help console. It internally calls python's help function.

# Signature
# help(object)  


# Calling function  
# info = help() # No argument  
# Displaying result  
# print(info)  



# info = help(1) # integer value  
# Displaying result  
# print(info)  


# info = help(list) # integer value  
# Displaying result  
# print(info)  


# info = help("Javatpoint") # integer value  
# Displaying result  
# print(info)  

# ************************************************************


# min() Function
# Python min() function is used to get the smallest element from the collection. This function takes two arguments, first is a collection of elements and second is key and returns the smallest element from the collection.

# Signature
# min (collection[, key])  


# collection: It is a comma-separated list of elements.

# key: Specifies a one-argument ordering function.

# Return
# It returns the smallest element from the collection.

# Let's see some examples of min() function to understand it's functionality.

# Python min() Function Example 1
# A simple example to get the smallest element from the collection. See the below example.

# Python min() function example  
# Calling function  
small = min(2225,325,2025) # returns smallest element  
small2 = min(1000.25,2025.35,5625.36,10052.50)  
# Displaying result  
print(small)  
print(small2)  




small = min('a','A','b','B') # returns smallest element  
small2 = min([10,12],[12,21],[13,15])  
# Displaying result  
print(small)  
print(small2)  



small = min("Python","Java","Scala") # returns smallest element  
small2 = min([10,12,33],[12,21,55],[13,15], key=len) # returns smallest element's length  
# Displaying result  
print(small)  
print(small2)  

# *************************************************************


# set() Function
# In python, a set is a built-in class, and this function is a constructor of this class. It is used to create a new set using elements passed during the call. It takes iterable as an argument and returns a new set object. The constructor syntax is given below.

# Signature
# set([iterable])  

result = set() # empty set  
result2 = set('12')  
result3 = set('javatpoint')  
# Displaying result  
print(result)  
print(result2)  
print(result3)  




result = set(['12','13','15'])  
result2 = set(('j','a','v','a','t','p','o','i','n','t'))  
result3 = set({1:'One',2:'Two',3:'Three'})  
# Displaying result  
print(result)  
print(result2)  
print(result3)  



def geteven(data):  
    if data%2 == 0:  
        return data  
      
evenval = filter(geteven,[2,5,6,9,8,4])  
# Calling function  
result = set(evenval)  
# Displaying result  
print(result)  


# **************************************************************************


# hex() Function
# Python hex() function is used to generate hex value of an integer argument. It takes an integer argument and returns an integer converted into a hexadecimal string. In case, we want to get a hexadecimal value of a float then use float.hex() function. The signature of the function is given below.

# Signature
# hex (integer) 


result = hex(1) # integer value  
result2 = hex(342)   
# Displaying result  
print(result)  
print(result2)  


result = float.hex(1.5) # float value  
result2 = float.hex(-238.15) # float value  
# Displaying result  
print(result)  
print(result2)

# ************************************************************************************


# id() Function
# Python id() function returns an identity of an object. This is an integer which is guaranteed to be unique. This function takes an argument an object and returns a unique integer number which represents identity. Two objects with non-overlapping lifetimes may have the same id() value.

# Signature
# id (object)  

val = id("Javatpoint") # string object  
val2 = id(1200) # integer object  
val3 = id([25,336,95,236,92,3225]) # List object  
# Displaying result  
print(val)  
print(val2)  
print(val3)  




# Python id() function example  
class Student:  
    def __init__(self, id, name):  
        self.id = id  
        self.name = name  
          
student = Student(101,"Mohan")          
print(student.id)  
print(student.name)  
# Calling function  
val = id(student) # student class object  
# Displaying result  
print("Object id:",val)  



# Python id() function example  
l1 = [1,2,3,4]  
l2 = [1,2,3,4]  
l3 = [3,5,6,7]  
# Calling function  
id1 = id(l1)  
id2 = id(l2)  
id3 = id(l3)  
# Displaying result  
print((l1==l2),(l1==l3))  
# Objects with the same values can have different ids  
print((id1==id2),(id1==id3))  
# l1 and l2 returns True, while id1 and id2 returns False  


# ********************************************************************************

# isinstance() Function
# Python isinstance() function is used to check whether the given object is an instance of that class. If the object belongs to the class, it returns True. Otherwise returns False. It also returns true if the class is a subclass.

# The isinstance() function takes two arguments object and classinfo and returns either True or False. The signature of the function is given below.

# Signature
# isinstance(object, classinfo) 

# class Student:  
#     id = 101  
#     name = "John"  
#     def __init__(self, id, name):  
#         self.id=id  
#         self.name=name  
  
# student = Student(1010,"John")  
# lst = [12,34,5,6,767]  
# # Calling function   
# print(isinstance(student, Student)) # isinstance of Student class  
# print(isinstance(lst, Student))  



# val = 10  
# lst = [12,34,5,6,767]  
# name = "Mohan"  
# # Calling function   
# print(isinstance(val, int)) # isinstance of int class  
# print(isinstance(lst, list)) # True  
# print(isinstance(name, str)) # True  
# print(isinstance(val, list)) # False  

# *****************************************************************
# oct() Function
# Python oct() function is used to get an octal value of an integer number. This method takes an argument and returns an integer converted into an octal string. It throws an error TypeError if argument type is other than an integer.

# The signature of oct() function is given below.

# Signature
# oct (integer)  


# val = oct(10)  
# # Displaying result  
# print("Octal value of 10:",val)  

# val = oct(10.25)  
# # Displaying result  
# print("Octal value of 10.25:",val)  



val  = oct(0b0101) # Binary to octal  
val2 = oct(0XAF) # Hexadecimal to octal  
# Displaying result  
# binary number  
print("Octal value of 0b0101:",val)  
# hexadecimal number  
print("Octal value of 0XAF:",val2)  


# *******************************************************************

# int() Function
# Python int() function is used to get the integer value. It returns an expression converted into an integer number. If the argument is a floating point, the conversion truncates the number. If the argument is outside the integer range, It converts the number into long type.

# If the number is not a number or if a base is given, the number must be a string.

# Signature
# int(x, base=10)  



val = int(10) # integer value  
val2 = int(10.52) # float value  
val3 = int('10') # string value  
# Displaying result  
print("integer values :",val, val2, val3)  