# The Python Random module is a built-in module for generating random integers in Python. These numbers occur randomly and does not follow any rules or instructuctions. We can therefore use this module to generate random numbers, display a random item for a list or string, and so on.
# The random() Function
# The random.random() function gives a float number that ranges from 0.0 to 1.0. There are no parameters required for this function. This method returns the second random floating-point value within [0.0 and 1] is returned.
# Python program for generating random float number  
import random    
num=random.random()    
print(num)    

# The randint() Function
# The random.randint() function generates a random integer from the range of numbers supplied.

# Python program for generating a random integer  
# import random  
num = random.randint(1, 500)  
print( num )  
