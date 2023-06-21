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
# To shuffle elements in the list  
list1 = [34, 23, 65, 86, 23, 43]    
random.shuffle( list1 )    
print( list1 )    
random.shuffle( list1 )    
print( list1 )    

# ******************************************************************************************************************


# Rock-Paper-Scissor Program using Random Module

# import random module  
import random  
# Function to play game  
def start_game():  
    # Print games rules and instructions  
    print(" This is Javatpoint's Rock-Paper-Scissors! ")  
    print(" Please Enter your choice: ")  
    print(" choice 1: Rock ")  
    print(" choice 2: Paper ")  
    print(" choice 3: Scissors ")  
#To take the user input      
choice_user = int(input(" Select any options from 1 - 3 : "))  
  
    # randint() Function which generates a random number by computer  
    choice_machine = random.randint(1, 3)  
  
    # display the machines choice  
    print(" Option choosed by Machine is: ", end = " ")  
    if choice_machine == 1:  
        print(" Rock ")  
    elif choice_machine == 2:  
        print("Paper")  
    else:  
        print("Scissors")  
  
    # To declare who the winner is  
    if choice_user == choice_machine:  
        print(" Wow It's a tie! ")  
    elif choice_user == 1 and choice_machine == 3:  
        print(" Congratulations!! You won! ")  
    elif choice_user == 2 and choice_machine == 1:  
        print(" Congratulations!! You won! ")  
    elif choice_user == 3 and choice_machine == 2:  
        print(" Congratulations!! You won! ")  
    else:  
        print(" Sorry! The Machine Won the Game? ")  
  
    # If user wants to play again  
    play_again = input(" Want to Play again? ( yes / no ) ").lower()  
    if play_again == " yes ":  
        start_game()  
    else:  
        print(" Thanks for playing Rock-Paper-Scissors! ")  
  
# Begin the game  
start_game()  


# *************************************************************************************************

# Various Functions of Random Module
# Following is the list of functions available in the random module.


# Function	Description
# seed(a=None, version=2)	This function creates a new random number.
# getstate()	This method provides an object reflecting the generator's present state. Provide the argument to setstate() to recover the state.
# setstate(state)	Providing the state object resets the function's state at the time getstate() was invoked.
# getrandbits(k)	This function provides a Python integer having k random bits. This is important for random number production algorithms like randrange(), which can manage arbitrarily huge ranges.
# randrange(start, stop[, step])	From the range, it produces a random integer.
# randint(a, b)	Provides an integer within a and b at random (both inclusive). If a > b, a ValueError is thrown.
# choice(seq)	Produce a non-empty series item at random.
# shuffle(seq)	Change the order.
# sample(population, k)	Display a list of k-size unique entries from the population series.
# random()	This function creates a new random number.
# uniform(a, b)	This method provides an object reflecting the generator's present state. Provide the argument to setstate() to recover the state.
# triangular(low, high, mode)	Providing the state object resets the function's state at the time getstate() was invoked.
# guass(mu, sigma)	With mean and standard deviation, a float number is generated randomly.
# betavariate(alpha, beta)	With alpha and beta, a float number is generated randomly between the range 0 and 1. - Beta Distribution
# expovariate(lambda)	Float number is generated by using the argument lambda. - Exponential Distribution
# normalvariate(mu, sigma)	With mean and standard deviation, a float number is generated randomly. - Normal Distribution
# gamavariate(alpha, beta)	With alpha and beta, a float number is generated randomly. - Gamma Distribution
