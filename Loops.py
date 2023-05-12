# while loop 

# i = 1
# while i < 6: 
#  print(i) 
#  i += 1 


# a=1
# while a<=10:
#     print(f"Sandeep Moorani {a}")
#     a=a+1

# sum of 10 numbers

# total=0
# i=1
# while i<=20:
#     # total += i
#     total=total+i
#     i= i + 1
#     print(total)


# total=0
# user_num=int(input("enter your number :"))
# i=1

# while i<=user_num:
#     total+=i
    
#     i+=1
#     print(total)

# ************************

# n=input("enter your digits more than 1:")
# # int(n[i]) 
# i=0
# total=0
# while i<len(n):
#     total+=int(n[i])
#     i+=1
#     print(total)
    

    # ****************************
# name=input("Enter your name please:")
# i=0
# temp_var=""
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var+=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i+=1

# infinite loop 

# M1

# i=0
# while i<=10:
#     print("sandeep moorani")


# M2

# while True:
#     print("Good Night")










# ********************************************************
# For loop 

# for i in range(5):
    # print("Software Engineering")

    # print(f"Sandeep Moorani : {i}")


# for i in range(1 ,11):
#     print(f"hi  : {i}")
#     print("hello \n")

# sum=0

# for i in range(1,11):
#     sum +=i
#     print(sum)



n=int(input("Enter your number:"))
sum=0

for i in range(1,n+1):
    sum+=i
    print(sum)