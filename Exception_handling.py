while True:
    try:
        age= int(input("enter your age :"))
        break
    except ValueError:
        print("invalid input")
    except:
        print("unexpected error....")


if age <18:
    print("not adult")
else:
    print("adult")
    
