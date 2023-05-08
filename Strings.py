#  strings
# x='Hello'
# y="Hello"

# x="""hello iam a software emgineer and iam learning first time programming language """
# print(x)


# "sandeep moorani".upper()
# "this is a string".upper()
#  "yes".strip()

# "hello is me" .count("l")

# String operations


# len(string) - Returns the length of the string

# for character in string - Iterates over each character in the string

# if substring in string - Checks whether the substring is part of the string

# string[i] - Accesses the character at index i of the string, starting at zero

# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).



# String methods




# string.lower() - Returns a copy of the string with all lowercase characters

# string.upper() - Returns a copy of the string with all uppercase characters

# string.lstrip() - Returns a copy of the string with the left-side whitespace removed

# string.rstrip() - Returns a copy of the string with the right-side whitespace removed

# string.strip() - Returns a copy of the string with both the left and right-side whitespace removed

# string.count(substring) - Returns the number of times substring is present in the string

# string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.

# string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.

# string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)

# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter

# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.

# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 




# example = "format() method"

# formatted_string = "this is an example of using the {} on a string".format(example)

# print(formatted_string)


# first = "apple"
# second = "banana"
# third = "carrot"

# formatted_string = "{0} {2} {1}".format(first, second, third)

# print(formatted_string)


# a="abc"
# b="xyz"
# c="a to z"

# fmethod= "{0} {2} {1}".format(a,b,c)
# print(fmethod)


# '{:d}'.format(10.5)

# ****************************************************


# def convert_distance(miles):
#     km = miles * 1.6 
#     result = "{} miles equals {:.1f} km" .format(miles,km)
#     return result
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# **************************************


# def nametag(first_name, last_name):
#     return("{} {}.".format(first_name,last_name[0]))


# print(nametag("Jane", "Smith")) 
# # Should display "Jane S." 
# print(nametag("Francesco", "Rinaldi")) 
# # Should display "Francesco R." 
# print(nametag("Jean-Luc", "Grand-Pierre")) 
# # Should display "Jean-Luc G." 

# # ***********************************

# def replace_ending(sentence, old, new):
#     # Check if the old substring is at the end of the sentence 
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the 
#         # end with the new string
#         i = len(sentence) - len(old)
#         new_sentence = sentence[:i] + new
#         return new_sentence


#     # Return the original sentence if there is no match 
#     return sentence
    
# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

# *********************************

# name = "Sadeep"
# age =20
# print("hello"+name+"your age is"+str(age))

# print("hello {} your age is {}".format(name,age))

# print(f"Hello {name} your age is {20}")

# **********************************

# first,second, third=input("enter your first ,second , third number").split()
# avg=int(first+second+third)/3
# print(f"Average of three numbers is {(int(first)+int(second)+int(third))/3}")


# print("{0} {1} {2}".format(first,second,third))
# print(f"{first} {second} {third}")

# *******************

# nmae ="Sandeep"
# print(nmae[3::-1])

# Name=input("Enter your Name:")
# print("your name is:"+Name[::-1])

# ************************

# Name="Sandeep Moorani"
# print(len(Name))
# print(Name.lower())
# print(Name.upper())
# print(Name.title())
# print(Name.count("o"))

# *****************

# name,single=input("Enter your name and sigle letter:").split()
# print(len(name))
# print(name.count(single)) 

# ******************

string="Iam a software engineer and iam studing at MUET"
print(string.replace(" ","_"))
print(string.find("a"))

Name="Sandeep"
print(Name.center(9,"*"))

name=input("enter your name:")
print(name.center(len(name)+10,"#"))



