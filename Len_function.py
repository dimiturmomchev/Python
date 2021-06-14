name = input("Write Name: ")

if len(name) < 3:
    print("Name must e at least 3 characters")
elif len(name) > 50:
    print("Name must be a miximum of 50 characters")
else:
    print("Names is correct")