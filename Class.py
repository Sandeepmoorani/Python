class Student:
    def __init__(self,name,rollno,district):
        self.name=name
        self.rollno=rollno
        self.district=district

s1= Student('Sandeep','21sw015','Tharparkar')
print(s1.district)



class Person:
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age

    def full_name(self):
        return f"{self.name}  {self.last_name}"
p1=Person('Sandeep','Moorani',20)
print(p1.full_name())


# ***********************************************************

class Employee:    
    id = 10   
    name = "John"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))    
# Creating a emp instance of Employee class  
emp = Employee()    
emp.display()    





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


class Student:    
    count = 0    
    def __init__(self):    
        Student.count = Student.count + 1    
s1=Student()    
s2=Student()    
s3=Student()    
print("The number of students:",Student.count)    
        
        # ******************************************** no parameter constuctor *************

class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()  
student.show("John")      





class Student:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = Student("John")  
student.show()    








class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
  
st = Student()  







# Python built-in class functions

# The built-in functions defined in the class are described in the following table.


# 1	getattr(obj,name,default)	It is used to access the attribute of the object.
# 2	setattr(obj, name,value)	It is used to set a particular value to the specific attribute of an object.
# 3	delattr(obj, name)      	It is used to delete a specific attribute.
# 4	hasattr(obj, name)	        It returns true if the object contains some specific attribute.




class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
    # creates the object of the class Student  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23  
setattr(s, "age", 23)  
  
# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
  
# this will give an error since the attribute age has been deleted  
# print(s.age)  