# Python Collection Module
# The Python collection module is defined as a container that is used to store collections of data, for example - list, dict, set, and tuple, etc. It was introduced to improve the functionalities of the built-in collection containers.

# Python collection module was first introduced in its 2.4 release.

# There are different types of collection modules which are as follows:

# namedtuple()
# The Python namedtuple() function returns a tuple-like object with names for each position in the tuple. It was used to eliminate the problem of remembering the index of each field of a tuple object in ordinary tuples.



# Examples:

pranshu = ('James', 24, 'M')    
print(pranshu)    

# OrderedDict()
# The Python OrderedDict() is similar to a dictionary object where keys maintain the order of insertion. If we try to insert key again, the previous value will be overwritten for that key.

# Example

import collections    
d1=collections.OrderedDict()    
d1['A']=10    
d1['C']=12    
d1['B']=11    
d1['D']=13    
    
for k,v in d1.items():    
    print (k,v)    

# **********************************************************************************

defaultdict()
# The Python defaultdict() is defined as a dictionary-like object. It is a subclass of the built-in dict class. It provides all methods provided by dictionary but takes the first argument as a default data type.
from collections import defaultdict      
number = defaultdict(int)      
number['one'] = 1      
number['two'] = 2      
print(number['three'])    

# **************************************************************************************
# Counter()
# The Python Counter is a subclass of dictionary object which helps to count hashable objects.

# Example

from collections import Counter      
c = Counter()    
list = [1,2,3,4,5,7,8,5,9,6,10]      
Counter(list)    
Counter({1:5,2:4})      
list = [1,2,4,7,5,1,6,7,6,9,1]      
c = Counter(list)      
print(c[1])     


# *******************************************************************************

# deque()
# The Python deque() is a double-ended queue which allows us to add and remove elements from both the ends.
list = ["x","y","z"]    
deq = deque(list)    
print(deq)  

# *************************************************************************************

Chainmap Objects
# A chainmap class is used to groups multiple dictionary together to create a single list. The linked dictionary stores in the list and it is public and can be accessed by the map attribute. Consider the following example.

baseline = {'Name': 'Peter', 'Age': '14'}  
adjustments = {'Age': '14', 'Roll_no': '0012'}  
print(list(ChainMap(adjustments, baseline)))  

# *************************************************************************

# UserDict Objects
# The UserDict behaves as a wrapper around the dictionary objects. The dictionary can be accessed as an attribute by using the UserDict object. It provides the easiness to work with the dictionary.

# It provides the following attribute.

# data - A real dictionary used to store the contents of the UserDict class.
# *********************************************************************************

# UserList Objects
# The UserList behaves as a wrapper class around the list-objects. It is useful when we want to add new functionality to the lists. It provides the easiness to work with the dictionary.

# It provides the following attribute.

# data - A real list is used to store the contents of the User class.
# *************************************************************************************

# UserString Objects
# The UserList behaves as a wrapper class around the list objects. The dictionary can be accessed as an attribute by using the UserString object. It provides the easiness to work with the dictionary.

# It provides the following attribute.


# data - A real str object is used to store the contents of the UserString class.
