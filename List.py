# updating list values  
# list = [1, 2, 3, 4, 5, 6]       
# print(list)       
# # It will assign value to the value to the second index     
# list[2] = 10     
# print(list)      
# # Adding multiple-element     
# list[1:3] = [89, 78]       
# print(list)     
# # It will add value at the end of the list    
# list[-1] = 25    
# print(list)    

# # concatenation of two lists  

# # declaring the lists  
# list1 = [12, 14, 16, 18, 20]  
# list2 = [9, 10, 32, 54, 86]  

# l = list1 + list2  
# print(l)  

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]  
# # finding length of the list  
# print(len(list1) ) 


# Adding elements to the list 

#Declaring the empty list    
# l =[]    
# #Number of elements will be entered by the user      
# n = int(input("Enter the number of elements in the list:"))    
# # for loop to take the input    
# for i in range(0,n):       
#     # The input is taken from the user and added to the list as the item    
#     l.append(input("Enter the item:"))       
# print("printing the list items..")     
# # traversal loop to print the list items      
# for i in l:     
#     print(i, end = "  ")   


# removing elements from list 

# list = [0,1,2,3,4]       
# print("printing original list: ");      
# for i in list:      
#     print(i,end=" ")      
# list.remove(2)      
# print("\nprinting the list after the removal of first element...")      
# for i in list:      
#     print(i,end=" ")    

# list1 = [103, 675, 321, 782, 2000,100]  
# # large element in the list  
# print(max(list1))  


# list1 = [103, 675, 321, 782,0, 200]  
# # smallest element in the list  
# print(min(list1)) 

# ************************************************

# Write the program to remove the duplicate element of the list.



list1 = [1,2,2,3,55,98,65,65,13,29]    
# Declare an empty list that will store unique values    
list2 = []    
for i in list1:    
    if i not in list2:    
        list2.append(i)    
print(list2)    



# Write a program to find the sum of the element in the list.



list1 = [3,4,5,9,10,12,24]    
sum = 0    
for i in list1:    
    sum = sum+i        
print("The sum is:",sum)  