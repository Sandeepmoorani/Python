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
        