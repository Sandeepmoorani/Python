# while True:
#     try:
#         age= int(input("enter your age :"))
#         break
#     except ValueError:
#         print("invalid input")
#     except:
#         print("unexpected error....")
#     else:
#         print("adult")
#         break
#     finally:
#         print("finally block")


# if age <18:
#     print("not adult")
# else:
#     print("adult")



def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  





# Sr.No.	Name of the Exception	Description of the Exception

# 1	Exception	All exceptions of Python have a base class.

# 2	StopIteration	If the next() method returns null for an iterator, this exception is raised.

# 3	SystemExit	The sys.exit() procedure raises this value.

# 4	StandardError	Excluding the StopIteration and SystemExit, this is the base class for all Python built-in exceptions.

# 5	ArithmeticError	All mathematical computation errors belong to this base class.

# 6	OverflowError	This exception is raised when a computation surpasses the numeric data type's maximum limit.

# 7	FloatingPointError	If a floating-point operation fails, this exception is raised.

# 8	ZeroDivisionError	For all numeric data types, its value is raised whenever a number is attempted to be divided by zero.

# 9	AssertionError	If the Assert statement fails, this exception is raised.

# 10	AttributeError	This exception is raised if a variable reference or assigning a value fails.

# 11	EOFError	When the endpoint of the file is approached, and the interpreter didn't get any input value by raw_input() or input() functions, this exception is raised.

# 12	ImportError	This exception is raised if using the import keyword to import a module fails.

# 13	KeyboardInterrupt	If the user interrupts the execution of a program, generally by hitting Ctrl+C, this exception is raised.

# 14	LookupError	LookupErrorBase is the base class for all search errors.

# 15	IndexError	This exception is raised when the index attempted to be accessed is not found.

# 16	KeyError	When the given key is not found in the dictionary to be found in, this exception is raised.

# 17	NameError	This exception is raised when a variable isn't located in either local or global namespace.

# 18	UnboundLocalError	This exception is raised when we try to access a local variable inside a function, and the variable has not been assigned any value.

# 19	EnvironmentError	All exceptions that arise beyond the Python environment have this base class.

# 20	IOError	If an input or output action fails, like when using the print command or the open() function to access a file that does not exist, this exception is raised.


# 22	SyntaxError	This exception is raised whenever a syntax error occurs in our program.

# 23	IndentationError	This exception was raised when we made an improper indentation.

# 24	SystemExit	This exception is raised when the sys.exit() method is used to terminate the Python interpreter. The parser exits if the situation is not addressed within the code.

# 25	TypeError	This exception is raised whenever a data type-incompatible action or function is tried to be executed.

# 26	ValueError	This exception is raised if the parameters for a built-in method for a particular data type are of the correct type but have been given the wrong values.

# 27	RuntimeError	This exception is raised when an error that occurred during the program's execution cannot be classified.

# 28	NotImplementedError	If an abstract function that the user must define in an inherited class is not defined, this exception is raised.