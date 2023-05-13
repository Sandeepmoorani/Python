# Functions 

# name = "Sandeep"
# print(len(name))

# 888888888888888888888


# def sum(a,b):
#     return a+b

# total=sum(1,2)
# print(total)

# x= int(input("Enter first number :"))
# y= int(input("Enter second number :"))

# total_sum= sum(x,y)
# print(total_sum)
 
# first_name= input("Enter first name : ")
# last_name= input("Enter last name  : ")
# print(sum(first_name,last_name))


# ******************************

# def last_char(name):
#     return name[-1]
# print(last_char("Sandeep"))


# *******************************

# def even_odd(num):
#     if num%2 ==0:
#         return "even"
#     else:
#         return "odd"
# print(even_odd(1))


# def is_even(numb):
#     if numb%2 ==0:
#         return True
#     return False    
# print(is_even(12))

# def is__Even(num):
#     return num%2==0 
# print(is__Even(23))

# *********************************

def is_greater(num,num1):
    if num >num1:
        return num
    else:
        return num1
x=int(input("enter your first num :"))
y=int(input("enter your sec num :"))
big=is_greater(x,y)
print(f"{big} Is greater" )
