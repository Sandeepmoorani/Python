# set data type 
# unordered collection of items 

# no indexing 
# no repeating element in sets only one times count 

x={1,2,3,4,5}
print(x)


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
