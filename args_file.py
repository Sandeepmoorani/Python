def total(*args):
    total=0
    for i in args:
        total +=i
    return total
print(total(2,4,6))




# **********************8

def multipy(*args):
    multipy=1
    for i in args:
        multipy *=i
    return multipy
print(multipy(2,3,4))


# *********************************** Lambda ***************************

add= lambda a,b : a+b
print(add(2,3))


multipy = lambda x,y : x*y
print(multipy(5,5))


# ************************************************************************

# parameter 
# *args 
# default_parameter 
# **kwargs 

def func(name,*args,last_name="Moorani",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
print(func('Sandeep',2,2,3 , x=2 ,y=4))

