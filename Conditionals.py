# if statement

# x=10
# y=20
# if x<y:
#     print("x is less than y" )
# a = 33
# b = 200
# if b > a: 
#   print("b is greater than a")

# elif a==b:
#       print("a equals to b")

# else:
#     print("a is greater than b")


# age=input("enter your age:")
# age=int(age)
# if age>=18:
#   print("your are eligible")
# else:
#     print("your are not eligible")

# *******************************

# WinNum=5
# GuessNum=int(input("Guess number :"))
# if GuessNum==WinNum:
#   print("your Win !!!")
# elif GuessNum<WinNum:
#   print("To Low")
# elif GuessNum>WinNum:
#   print("To high")
# else:
#   print("Dont worry next time")

# *******************************

# and operator  when both conditions are ture 

# Name = 'Sandeep'
# RollNo=15
# if Name=='Sandeep' and RollNo==15:
#   print("Condition ture!")
# else:
#   print("Condition false!")


# or operator  when one  conditions is ture 

#   Name = 'Sandeep'
# RollNo=15
# if Name=='Sandeep' or RollNo==21:
#   print("Condition ture!")
# else:
#   print("Condition false!")

# ********************************


# Name,age=input("enter your name and age:").split()
User_Name=input("enter your name:")
User_age=int(input("enter your age:"))
if User_age >=10 and (User_Name[0]=='a' or User_Name[0]=='A'):
  print("You can watch movie ")
else:
  print("you cannot watch movie")


