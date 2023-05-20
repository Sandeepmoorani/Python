# Python is an object-oriented language 
# Major principles of object-oriented programming system are given below.

# Class
# Object
# Method
# Inheritance
# Polymorphism
# Data Abstraction
# Encapsulation


# *************************************** Class*****************************


# The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods. For example: if you have an employee class, then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

# Syntax

# class ClassName:     
#         <statement-1>     
#         .     
#         .      
#         <statement-N>     


# ******************************************** Object **************************



# The object is an entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.

# Everything in Python is an object, and almost everything has attributes and methods. All functions have a built-in attribute __doc__, which returns the docstring defined in the function source code.

# When we define a class, it needs to create an object to allocate the memory. Consider the following example.

# Example:

class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()  

