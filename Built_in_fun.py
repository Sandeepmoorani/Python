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