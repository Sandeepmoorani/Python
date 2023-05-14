# Lists in Python are defined using square brackets, with the elements stored in the list separated by commas:
#  list = ["This", "is", "a", "list"]
#  You can use the len() function to return the number of elements in a list: len(list) would return 4.


# a=[1,2,3,4,5,6,7,8,9,10]
# print(a)

# b=["Hi","iam", "sandeep", "Moorani","My","RollNo","is:","21sw015"]

# b.append("Software")
# b.insert(0,"hello")
# c=a+b
# print(c)

# a.extend(b)
# print(a)
# print(b)
# ***************************************

# fruits=["Banana","Grapes"]
# fruits1=["Apple","Mango"]

# fruits.append("cheku")
# fruits.insert(1,"papeto")
# fruits.extend(fruits1)

# print(fruits)
# print(fruits1)

fruits=["Apple","Mango","Banana","Grapes","Apple"]
# fruits.pop(2)
# fruits.insert(2,"Mango")
# fruits.remove("Apple")
# print(fruits)

# if "Apple" in fruits:
#     print('yes apple is present')
# else:
#     print("Apple is not present")

# Count
# print(fruits.count("Apple"))

# Sort 
# fruits.sort()
num=[1,2,10,9,5,67,8]
# print(sorted(num))
# print(fruits)

# copy() 
num1=num.copy()
print(num1)


# a = ["We", "are", "learning"]
# print(type(a))

# print(a)
# print(a[1])
# #   through index
# print(a[1:3])
# print(a[:2])

# len(a)


# x = "Sandeep moorani"
# len(x)

# # append

# fruits = ["Banana", "Apple", "orange"]
# fruits.append("Mango")
# print(fruits)

# # insert
# fruits.insert(0, "papeto")
# print(fruits)

# you can add any element at any index no error occured

# remove , pop

# fruits.remove("papeto")
# print(fruits)
# fruits.pop(0)
# print(fruits)

# fruits[2] = "fruity"
# print(fruits)


# multipe = []
# for x in range(1, 11):
#     multipe.append(x * 8)
#     print(multipe)

    # *********************

    ## Simple List Comprehension
# print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
# print([x * 2 for x in range(1, 11)])


### Long form for loop
# print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
# my_list = []
# for x in range(1, 11):
#     my_list.append(x * 2)
# print(my_list)

# **********************

# Common sequence operations


# Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations are used by both lists and tuples:

# len(sequence) - Returns the length of the sequence.

# for element in sequence - Iterates over each element in the sequence.

# if element in sequence - Checks whether the element is part of the sequence.

# sequence[x] - Accesses the element at index [x] of the sequence, starting at zero

# sequence[x:y] - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

# for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time.

# List-specific operations and methods
# One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). There are a few operations and methods that are specific to changing data within lists:

# list[index] = x - Replaces the element at index [n] with x.

# list.append(x) - Appends x to the end of the list.

# list.insert(index, x) - Inserts x at index position [index].

# list.pop(index) - Returns the element at [index] and removes it from the list. If [index] position is not in the list, the last element in the list is returned and removed.

# list.remove(x) - Removes the first occurrence of x in the list.

# list.sort() - Sorts the items in the list.

# list.reverse() - Reverses the order of items of the list.

# list.clear() - Deletes all items in the list.

# list.copy() - Creates a copy of the list.

# list.extend(other_list) - Appends all the elements of other_list at the end of list


# List comprehensions


# A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code. It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can be difficult to interpret by other coders.

# [expression for variable in sequence] - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.

# Example: my_list = [ x*2 for x in range(1,11) ]

# [expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true.

# Example: my_list = [ x for x in range(1,101) if x % 10 == 0 ]


# Lists in Python are defined using square brackets, with the elements stored in the list separated by commas:
#  list = ["This", "is", "a", "list"]
#  You can use the len() function to return the number of elements in a list: len(list) would return 4.

# a = ["We", "are", "learning"]
# print(type(a))

# print(a)
# print(a[1])
# #   through index
# print(a[1:3])
# print(a[:2])

# len(a)


# x = "Sandeep moorani"
# len(x)

# # append

# fruits = ["Banana", "Apple", "orange"]
# fruits.append("Mango")
# print(fruits)

# # insert
# fruits.insert(0, "papeto")
# print(fruits)

# # you can add any element at any index no error occured

# # remove , pop

# fruits.remove("papeto")
# print(fruits)
# fruits.pop(0)
# print(fruits)

# fruits[2] = "fruity"
# print(fruits)


# multipe = []
# for x in range(1, 11):
#     multipe.append(x * 8)
#     print(multipe)

    # *********************

    ## Simple List Comprehension
# print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
# print([x * 2 for x in range(1, 11)])


### Long form for loop
# print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
# my_list = []
# for x in range(1, 11):
#     my_list.append(x * 2)
# print(my_list)

# **********************

# Common sequence operations


# Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations are used by both lists and tuples:

# len(sequence) - Returns the length of the sequence.

# for element in sequence - Iterates over each element in the sequence.

# if element in sequence - Checks whether the element is part of the sequence.

# sequence[x] - Accesses the element at index [x] of the sequence, starting at zero

# sequence[x:y] - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

# for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time.

# List-specific operations and methods
# One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). There are a few operations and methods that are specific to changing data within lists:

# list[index] = x - Replaces the element at index [n] with x.

# list.append(x) - Appends x to the end of the list.

# list.insert(index, x) - Inserts x at index position [index].

# list.pop(index) - Returns the element at [index] and removes it from the list. If [index] position is not in the list, the last element in the list is returned and removed.

# list.remove(x) - Removes the first occurrence of x in the list.

# list.sort() - Sorts the items in the list.

# list.reverse() - Reverses the order of items of the list.

# list.clear() - Deletes all items in the list.

# list.copy() - Creates a copy of the list.

# list.extend(other_list) - Appends all the elements of other_list at the end of list


# List comprehensions


# A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code. It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can be difficult to interpret by other coders.

# [expression for variable in sequence] - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.

# Example: my_list = [ x*2 for x in range(1,11) ]

# [expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true.

# Example: my_list = [ x for x in range(1,101) if x % 10 == 0 ]
