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
