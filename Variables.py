# Variables are containers that store information

name = "Abhishek"   #type str
age = 20            #type int
passed = True       #type bool



# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable name must start with a letter or the underscore character.
# Variables are case sensitive.
# Variable name cannot start with a number.

Color = "yellow"    #valid variable name
cOlor = "red"       #valid variable name
_color = "blue"     #valid variable name

# 5color = "green"    #invalid variable name
# $color = "orange"   #invalid variable name



NameOfCity = "Mumbai"       #Pascal case
nameOfCity = "Berlin"       #Camel case
name_of_city = "Moscow"     #snake case



# Local Variable:
# A local variable is created within a function and can be only used inside that function. Such a variable has a local scope.

icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")

foods()


# ************************

# Global Variable:
# A global variable is created in the main body of the code and can be used anywhere within the code. Such a variable has a global scope.

icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")
    print(fruit+"fruit is also local variable vale")

foods()
print(icecream + " is a global variable value.")
# print(fruit+ " is a local variable value.")


