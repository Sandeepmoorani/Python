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
code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
code = compile(code_str, 'sum.py', 'exec')  
print(type(code))  
exec(code)  
exec(x)  