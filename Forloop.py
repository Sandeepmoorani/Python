# A Closer Look at the Range() Function
# The in keyword, when used with the range() function, generates a sequence of integer numbers, which can be used with a for loop to control the start point, the end point, and the incremental values of the loop.  

# Syntax:

# 123
# for n in range(x, y, z):
#     print(n)

# The range() function uses a set of indices that point to integer values, which start at the number 0. The numeric values 0, 1, 2, 3, 4 correlate to ordinal index positions 1st, 2nd, 3rd, 4th, 5th. So, when a range call to the 5th index position is made using range(5) the index is pointing to the numeric value of 4.

# Index Number

# 1st index

# 2nd index

# 3rd index

# 4th index

# 5th index

# Value

# 0

# 1

# 2

# 3

# 4

# The range() function can take up to three parameters:  range(start, stop, step) 

# Start 
# The first item in the range() function parameters is the starting position of the range. The default is the first index position, which points to the numeric value 0. This value is included in the range. 

# Stop
# The second item in the range() function parameters is the ending position of the range. There is no default index position, so this index number must be given to the range() parameters. For example, the line for n in range(4) will loop 4 times with the n variable starting at 0 and looping 4 index positions: 0, 1, 2, 3. As you can see, range(4) (meaning index position 4) ends at the numeric value 3. In Python, this structure may be phrased as “the end-of-range value is excluded from the range.” In order to include the value 4 in  range(4), the syntax can be written as range(4+1) or range(5). Both of these ranges will produce the numeric values 0, 1, 2, 3, 4. 

# Step
# The third item in the range() function parameters is the incremental step value. The default increment is +1. The default value can be overridden with any valid increment. However, note that the loop will still end at the end-of-range index position, regardless of the incremental value. For example, if you have a loop with the range: for n in range(1, 5, 6), the range will only produce the numeric value 1. This is because the incremental value of 6 exceeded the ending point of the range.


# Practice Exercise
# You can use the code block below to test the values of n with various range() parameters. A few suggestions to test are:

# range(stop)

# range(3) 

# range(3+1) 

# range(start, stop)

# range(2, 6)     

# range(5,10+1) 

# range(start, stop, step)

# range(4, 15+1, 2)         

# range(2*2, 25, 3+2) 

# range(10, 0, -2)  

# for n in range(1, 5, 6):  
#     print(n)

#     for n in range(0,11,2):
#     print(n)



#     for number in range(2,7+1):
#     print(number*3)


# for x in range(2, -2, -1):
#     print(x)

# Key takeaways
# The roles of the range(start, stop, step) function parameters are:

# Start - Beginning of range

# value included in range

# default = 0

# Stop - End of range

# value excluded from range (to include, use stop+1)

# no default

# must provide the ending index number 

# Step - Incremental value 

# default = 1


# Study Guide: for Loops
# This study guide provides a summary of what you learned in this segment and serves as a guide for the upcoming practice quiz.  

# In the for Loops segment, you learned about the logical structure and syntax of for loops. You took a closer look at the range() function. You learned about nested for loops and complex nested for loops with if statements. You also learned how to fix common errors in for loops.


# for Loops vs. while Loops
# for loops and while loops share several characteristics. Both loops can be used with a variety of data types, both can be nested, and both can be used with the keywords break and continue. However, there are important differences between the two types of loops: 

# while loops are used when a segment of code needs to execute repeatedly while a condition is true

# for loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence

# Syntax 
# The syntax of a for loop with the in keyword:


# for variable in sequence:
#     body of loop


# Common for Loop Structures 
# for Loop with range()
# The in keyword with the range() function generates a sequence of integer numbers, which can be used with a for loop to configure the iterations of the code. The range of numbers [0, 1, 2] correlates to ordinal index positions (1st, 2nd, 3rd), rather than the cardinal (quantity) values of the numbers 0, 1, and 2. For example, range(5) means the five index positions in the range [0, 1, 2, 3, 4]. 

# The range() function can take up to three parameters. The roles of the three possible range(x,y,z) parameters are:

# x = Start - Starting index position of the range 

# Default index position is 0.

# The starting index position is included in the range. 

# Example syntax: range(2, y, z) or range(x+3, y, z) 

# y = Stop - Ending index position of range

# No default index position. Must include the ending index position in the range() parameters.

# Example syntax: range(y)

# The value of the ending index position is excluded from the range. 

# To include the ending index number, use the expression: y+1 (index + 1)

# Example syntax: range(x, y+1, z)

# Alternatively, if y = 10, you can write: range(x, 11, z)

# z = Step - Incremental value

# Default increment is +1.

# The default value can be overridden with any valid increment.

# The incremental value will end the for loop before it reaches the end of range index position (end of range index minus 1).  



# for number in range(1,6+1,2):
#     print(number*3)


# for number in range(2,8):
#     print(number**2)

# for x in sequence:
    # start of the outer loop body
    # for y in sequence:
        # start of the inner loop body

        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body


# for x in range(2):
#     print("This is the outer loop iteration number " + str(x))
#     for y in range(3+1):
#         print("Inner loop iteration number " + str(y))
#     print("Exit inner loop") 

# for n in range(6,18,3):
#     print(n*2)

# for n in range(6,18,3):
#     print(n+2)

# for n in range(6,18+1,3):
#     print(n*2)

# for n in range(19):
#     if n % 2 == 0:
#         print(n)

# for n in range(18+1):
#     print(n**2)

# for n in range(0,18+1,2):
#     print(n*2)

# for n in range(10):
#     print(n+n)



# Terms
# variables - Know how to properly initialize or increment a variable. You will also need to recognize a coding error due to the failure to properly initialize or increment a variable.

# infinite loops - Know how to recognize infinite loops and use common solutions to prevent them. For example, check loop conditions, ranges, iterators, control statements, etc. to ensure that at least one of these controls are in place to prevent an infinite loop.

# iterators - Know the various options available for iterating a variable (e.g., using assignment operators, using the third range() function parameter). You will also need to analyze where the iteration should occur. A misplaced iterator could produce the wrong output or create an infinite loop.  

# control statements - Know how and when to use the break and continue control statements to prevent infinite loops.  


# Common Functions
# range() Function Parameters - Know the roles of the three possible range(x, y, z) function parameters:

# x Start of Range (included)

# y End of Range (excluded index) 

# To include the end of range index, use the expression y+1

# The end of range must be included in the range() parameters.

# z Incremental value

# Example 1: range(4, 12+1, 2)

# This example creates a range that starts at 4 and ends at 12 (without the +1, the range would end at 11). 

# The third parameter increments the range iteration by 2, as opposed to the default increment of 1. The  range(4, 12+1, 2) expression would produce the values: 4, 6, 8, 10, 12 

# Example 2: range(10, 2-1, -2)

# This example creates a range that starts at 10 and ends at 2-1, with a decremental value of -2. When counting down, to include the value of the end of the range index, use -1 (end of range minus 1). This range produces the sequence: 10, 8, 6, 4, 2 


# print() Function Default Behavior - Know the default behavior of the print() function is to insert a new line character after the print statement runs.

# To override the insertion of the new line character and replace it with a space, add end=" " as the last item in the print() parameters. This makes it possible to add the next print output to the same line, separated by a space. You might use this technique when a print() function is part of a for or while loop. Example syntax:  print(x+1, end=" ")