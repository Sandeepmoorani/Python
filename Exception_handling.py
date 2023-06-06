try:
    age= int(input("enter your age :"))
except:
    print("invalid input")
if age <18:
    print("not adult")
else:
    print("adult")