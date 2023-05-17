# Python Tuples

# ordered collection of items 

# A Python Tuple is a group of items that are separated by commas. The indexing, nested objects, and repetitions of a tuple are somewhat like those of a list, however unlike a list, a tuple is immutable.

# The distinction between the two is that while we can edit the contents of a list, we cannot alter the elements of a tuple once they have been assigned.

# Creating an empty tuple    
# empty_tuple = ()    
# print("Empty tuple: ", empty_tuple)    
    
# # Creating tuple having integers    
# int_tuple = (4, 6, 8, 10, 12, 14)    
# print("Tuple with integers: ", int_tuple)    
    
# # Creating a tuple having objects of different data types    
# mixed_tuple = (4, "Python", 9.3)    
# print("Tuple with different data types: ", mixed_tuple)    
    
# # Creating a nested tuple    
# nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
# print("A nested tuple: ", nested_tuple)    


# *******************************************************

# numbers=(1,2,3,4,5)

# for i in numbers:
#     print(i)


# creating single tuples  *******************************************
single_tuple = ("Tuple",)    
print( type(single_tuple) )     
# Creating tuple without parentheses    
single_tuple = "Tuple",    
print( type(single_tuple) )    



# ************************************* access the tuples elements 

tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
print(tuple_[0])      
print(tuple_[1])   

# negative indexing 

tuple_ = ("Python", "Tuple", "Ordered", "Collection")    
# Printing elements using negative indices    
print("Element at -1 index: ", tuple_[-1])    
print("Elements between -4 and -1 are: ", tuple_[-4:-1])  