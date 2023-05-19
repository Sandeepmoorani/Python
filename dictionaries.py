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

    # ************************* delete in dictionary ************************************

poped_elmt= Emp_Info.pop('age')
print(poped_elmt)
print(Emp_Info)


# ***************************** cubefinder **********************************

def cube_finder(n):
    cubes={}

    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes
print(cube_finder(10))



# ****************************** square finder **************************


def square_finder(n):
    squares={}
    for i in range(1,n+1):
        squares[i]=i**2
    return squares
print(square_finder(10))


# **********************************************************************

Employee = {"Name": "Sandeep", "Age": 20, "salary":555000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print("Name : %s" %Employee["Name"])    
print("Age : %d" %Employee["Age"])    
print("Salary : %d" %Employee["salary"])    
print("Company : %s" %Employee["Company"])    


# ******************  input from user ***********************************  

# print("Enter the details of the new employee....");      
# Employee["Name"] = input("Name: ");      
# Employee["Age"] = int(input("Age: "));      
# Employee["salary"] = int(input("Salary: "));      
# Employee["Company"] = input("Company:");      
# print("printing the new data");      
# print(Employee) 



# ********************************* Built-in Dictionary methods *****************

# clear() method  

dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
print(dict)
dict.clear()  
print(dict)  


# copy() method  


dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
dict_demo = dict.copy()  
print(dict_demo)  



# pop() method  


dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
dict_demo = dict.copy()  
x = dict_demo.pop(1)  
print(x)  