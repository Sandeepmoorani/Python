while True:
    try:
        age= int(input("enter your age :"))
        break
    except ValueError:
        print("invalid input")
    except:
        print("unexpected error....")
    else:
        print("adult")
        break
    finally:
        print("finally block")


# if age <18:
#     print("not adult")
# else:
#     print("adult")
    
