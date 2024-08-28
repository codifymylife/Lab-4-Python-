print("Menu")
print("_____________")
print("1. Pyhton\n2. Java\n3. C#\n4. C")
#choice match case condition
try:
 ch = int(input("Enter your choice: "))
 match ch:
    case 1:
        print("My fav lang is: Python")
    case 2:
        print("My fav kang is: Java")
    case 3:
        print("My fav lang is: C#")
    case 4:
        print("My fav lang is: C")
    case _:
        print("Input is not between 1 to 4")
except:
    print("Invalid input format")