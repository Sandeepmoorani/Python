# while True:
#     try:
#         age= int(input("enter your age :"))
#         break
#     except ValueError:
#         print("invalid input")
#     except:
#         print("unexpected error....")
#     else:
#         print("adult")
#         break
#     finally:
#         print("finally block")


# if age <18:
#     print("not adult")
# else:
#     print("adult")



def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )  