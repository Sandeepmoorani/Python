# A constructor is a special type of method (function) which is used to initialize the instance members of the class.

# In C++ or Java, the constructor has the same name as its class, but it treats constructor differently in Python. It is used to create an object.


# Constructors can be of two types.

# Parameterized Constructor
# Non-parameterized Constructor

class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
emp1 = Employee("John", 101)  
emp2 = Employee("David", 102)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display()  