pro_num = int(input("Enter product number: "))

#condition
if(pro_num == 1):
    pro_am = int(input("Enter product amount: "))
    u_price = 5.00
    price = float(pro_am * u_price)
elif (pro_num == 2):
    pro_am = int(input("Enter product amount: "))
    u_price = 4.50
    price = float(pro_am * u_price)
elif (pro_num == 3):
    pro_am = int(input("Enter product amount: "))
    u_price = 2.99
    price = float(pro_am * u_price)
elif (pro_num == 4):
    pro_am = int(input("Enter product amount: "))
    u_price = 15.99
    price = float(pro_am * u_price)
elif (pro_num == 5):
    pro_am = int(input("Enter product amount: "))
    u_price = 59.99
    price = float(pro_am * u_price)
else:
    print("input error")
print("\n")
if pro_num>=1 and pro_num<=4:
    print(f"Selected product number :{pro_num}\nProduct unit price :RM{u_price}\nQuantity sold :{pro_am}\nTotal Price :{round(price, 2)}")