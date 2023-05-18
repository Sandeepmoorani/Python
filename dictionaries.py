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


# add data to an empty dictionary 
user={}
user['Nmae']='SandeepMoorani'
user['age']=20
print(user)

# check key exist in dictionary 

if 'Nmae' in user:
    print("yes exist")
else:
    print("not exist")


    # loops in dictionaries 
for i in Emp_Info.values():
    print(i)

for i in Emp_Info:
    print(i)


# print(Emp_Info.items)
A=Emp_Info.items()
print(A)


for key,value in Emp_Info.items():
    print(f"key is {key} : value is {value}")



    # *********************Addd element in dictionary *********************************
Emp_Info['district']='Tharparkar'
print(Emp_Info)

poped_elmt= Emp_Info.pop('age')
print(poped_elmt)
print(Emp_Info)
