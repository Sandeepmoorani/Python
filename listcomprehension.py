# create a list of square from 1 to 10 

square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

# same problem in list comprehension  

square2=[i**2 for i in range(1,11)]
print(square2)


# *******************************************************

neg_num=[]
for i in range(1,11):
    neg_num.append(-i)
print(neg_num)


# same problem in list comprehension  

negt_num=[-i for i in range(1,11)]
print(negt_num)


# ***********************************
names=['Sandeep','Sohail','Khushal','Lachman']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)



# same problem in list comprehension  

new_list1=[name[0] for name in names]
print(new_list1)


# ***********************************************


def reverse_string(l):
    return [namees[::-1] for namees in l]
print(reverse_string(['sandeep','Moorani','shahib']))


numb=list(range(1,11))
# print(numb)
even_list=[i for i in numb if i%2==0]
print(even_list)


odd_list=[i for i in numb if i%2 !=0]
print(odd_list)