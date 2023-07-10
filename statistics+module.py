# Python statistics module
# Python statistics module provides the functions to mathematical statistics of numeric data. There are some popular statistical functions defined in this module.


# mean() function
# The mean() function is used to calculate the arithmetic mean of the numbers in the list.


# exp

import statistics    
# list of positive integer numbers   
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)     
# Printing the mean   
print("Mean is :", x)  

# **********************************************************************

# median() function
# The median() function is used to return the middle value of the numeric data in the list.

# Example

import statistics     
datasets = [4, -5, 6, 6, 9, 4, 5, -2]      
# Printing median of the   
# random data-set   
print("Median of data-set is : % s "  
        % (statistics.median(datasets)))  

# Output:

# Median of data-set is : 4.5
