# # set data type 
# A Python set is the collection of the unordered items. Each element in the set must be unique, immutable, and the sets remove the duplicate elements. Sets are mutable which means we can modify it after its creation.

x={1,2,3,4,5}
print(x)

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    


# remove duplicate 
l=[1,2,3,3,4,4,32,23,3,2,2,3,45,5,6,7,8,8,9,8]
x2=list(set(l))
print(x2)


# add element in sets 

x.add(6)
x.add(7)
x.add(8)
x.add(9)
x.add(10)
x.add(11)
print(x)


# remove element in sets

x.remove(11)
print(x)

# discard()

x.discard(10)
print(x)

# clear()


x2.clear()
print(x2)

# for loop in sets

for items in x:
    print(items)


    # in sets we perform two operation 

    # 1)   Union 
    # 2)   intersection 

s1={1,2,3,4,5}
s2={2,3,5,6,7,8,9,10}
union_set=s1  | s2
print(union_set)


intersection_set= s1 & s2
print(intersection_set)


# substriction 
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2) #{"Wednesday", "Thursday" will be printed}    

#  Using difference() method

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2    



# Symmetric Difference of two sets
# The symmetric difference of two sets is calculated by ^ operator or symmetric_difference() method. Symmetric difference of sets, it removes that element which is present in both sets. Consider the following example:

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)  


# Using symmetric_difference() method

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)  
print(c)  