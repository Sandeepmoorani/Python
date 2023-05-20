# Lambda Functions in Python are anonymous functions, implying they don't have a name.

# Syntax of Python Lambda Function

# lambda arguments: expression       

add = lambda num: num + 4  
print( add(6) )  

# same as 
def add( num ):  
   return num + 4  
print( add(6) )  

# **************************************************************************

# Python code to show the reciprocal of the given number to highlight the difference between def() and lambda().  
def reciprocal( num ):  
    return 1 / num  
   
lambda_reciprocal = lambda num: 1 / num  
   
# using the function defined by def keyword  
print( "Def keyword: ", reciprocal(6) )  
   
# using the function defined by lambda keyword  
print( "Lambda keyword: ", lambda_reciprocal(6) )  


# **************************************** lambda with filter() ************************

# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
  

print(odd_list)  


# ******************************** lambda with map()************************

#Code to calculate the square of each number of a list using the map() function  
  
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]  
  
squared_list = list(map( lambda num: num ** 2 , numbers_list ))  
  
print( squared_list )  