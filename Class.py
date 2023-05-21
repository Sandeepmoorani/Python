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
        