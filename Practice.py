# number=10
# if number > 11: 
#   print(0)
# elif number != 10:
#   print(1)
# elif number >= 20 or number < 12:
#   print(2)
# else:
#    print(3)


# n = 4
# if n*6 > n**2 or n%2 == 0:
#     print("Check")




# def sum(x, y):
#         return(x+y)
# print(sum(sum(1,2), sum(3,4)))



# ((10 >= 5*2) and (10 <= 5*2))



# def greater_value(x, y):
#     if x > y:
#         return x
#     else:
#        return y

# print(greater_value(10,3*5))




# def difference(x, y):
#     z = x - y
#     return z


# print(difference(5, 3))



# number = 2   # Initialize the variable 
# while number <= 12:   # Complete the while loop condition
#     print(number, end=" ")
#     number +=2 # Increment the variable

# Should print 2 4 6 8 10 12 



# for number in range(2,13,2):
#     print(number)

# def even_numbers(n):
#     count = 0
#     current_number = 0
#     while current_number <=n: # Complete the while loop condition
#         if current_number % 2 == 0:
#              count += 1 # Increment the appropriate variable
#         current_number += 1 # Increment the appropriate variable
#     return count
    
# print(even_numbers(25))   # Should print 13
# print(even_numbers(144))  # Should print 73
# print(even_numbers(1000)) # Should print 501
# print(even_numbers(0))    # Should print 1


# def sequence(low, high):
#     # Complete the outer loop range to make the loop run twice
#     # to create two rows
#     for x in range(2): 
#         # Complete the inner loop range to print the given variable
#         # numbers starting from "high" to "low" 
#         # Hint: To decrement a range parameter, use negative numbers
#         for y in range(high, low-1, -1): 
#             if y == low:
#                 # Don’t print a comma after the last item
#                 print(str(y)) 
#             else:
#                 # Print a comma and a space between numbers
#                 print(str(y), end=", ") 

# sequence(1, 3)
# # Should print the sequence 3, 2, 1 two times, as shown above.

# for sum in range(5):
#     sum += sum
#     print(sum)

for x in range(10):
    for y in range(x):
        print(y)