# How to create a dictionary 

# Two methods to create a dictionary 

name={'Name':'Sandeep','age':20}
print(name)

print(type(name))

# another way 

Name=dict(Name="Sandeep",age=20)
print(Name)
print(type(Name))

# ********************** How to acces data in dictionary **************************

# we access data in dictionary through key not through index 

print(Name['age'])

Emp_Info={
    'name':'Sandeep',
    'age':20,
    'rollno':15,
    'dept':'software'
}

print(Emp_Info)
print(Emp_Info['rollno'])