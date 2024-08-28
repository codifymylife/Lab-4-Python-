num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))

#condition
if(num_1>num_2):
    print(f"{num_1} is greater than {num_2}")
elif(num_1<num_2):
    print(f"{num_2} is greater than {num_1}")
else:
    print(f"Both numbers are equal")