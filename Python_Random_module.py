# The Python Random module is a built-in module for generating random integers in Python. These numbers occur randomly and does not follow any rules or instructuctions. We can therefore use this module to generate random numbers, display a random item for a list or string, and so on.
# The random() Function
# The random.random() function gives a float number that ranges from 0.0 to 1.0. There are no parameters required for this function. This method returns the second random floating-point value within [0.0 and 1] is returned.
# Python program for generating random float number  
import random    
num=random.random()    
print(num)    

# ********************************************************************************

# The randint() Function
# The random.randint() function generates a random integer from the range of numbers supplied.

# Python program for generating a random integer  
# import random  
num = random.randint(1, 500)  
print( num )  



# ***********************************************************************
The randrange() Function
# The random.randrange() function selects an item randomly from the given range defined by the start, the stop, and the step parameters. By default, the start is set to 0. Likewise, the step is set to 1 by default.


# To generate value between a specific range  
# import random    
num = random.randrange(1, 10)    
print( num )    
num = random.randrange(1, 10, 2)    
print( num )                


# # *********************************************************
# The choice() Function
# The random.choice() function selects an item from a non-empty series at random. In the given below program, we have defined a string, list and a set. And using the above choice() method, random element is selected.

# To select a random element  
# import random  
random_s = random.choice('Random Module') #a string  
print( random_s )  
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list  
print( random_l )  
random_s = random.choice((12, 64, 23, 54, 34)) #a set  
print( random_s )  
# # ********************************************************************************************
# The shuffle() Function
# The random.shuffle() function shuffles the given list randomly.
