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



# mode() function
# The mode() function returns the most common data that occurs in the list.


# Example

import statistics     
# declaring a simple data-set consisting of real valued positive integers.   
dataset =[2, 4, 7, 7, 2, 2, 3, 6, 6, 8]     
# Printing out the mode of given data-set   
print("Calculated Mode % s" % (statistics.mode(dataset)))  


# Output:

# Calculated Mode 2

# stdev() function
# The stdev() function is used to calculate the standard deviation on a given sample which is available in the form of the list.

# Example

import statistics     
# creating a simple data - set   
sample = [7, 8, 9, 10, 11]     
# Prints standard deviation   
print("Standard Deviation of sample is % s "   
                % (statistics.stdev(sample)))   
# Output:

# Standard Deviation of sample is 1.5811388300841898
# ************************************************************************************************



# median_low()
# The median_low function is used to return the low median of numeric data in the list.


# Example

import statistics     
# simple list of a set of integers   
set1 = [4, 6, 2, 5, 7, 7]     
# Note: low median will always be a member of the data-set.     
# Print low median of the data-set   
print("Low median of data-set is % s "   
        % (statistics.median_low(set1)))  


# Output:

# Low median of the data-set is 5


# **************************************************************************************************************
