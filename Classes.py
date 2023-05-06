# We start with the class keyword,
#  After the class definition line is the class body, indented to the right. Inside the class body, we can define attributes for the class.
class Apple:
     color = ""
     flavor = ""



jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"



# **************************

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    # Exchange all the apples
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    # Share and sum up the ideas
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



# ***********************************

def max_elevation_city(min_population):
    # Initialize the variable that will hold the information of the city with the highest elevation 
    return_city = City()

    # Evaluate the 1st instance to meet the requirements
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1

    # Evaluate the 2nd instance to meet the requirements
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2

    # Evaluate the 3rd instance to meet the requirements
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


# **************************************


