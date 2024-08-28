print("Menu")
print("--------------")
print(f"1. Python")
print(f"2. Java")
print(f"3. C#")
print(f"4. C")
ch = int(input("Enter your choice: "))
#condition
if(ch==1):
    ch = "Python"
    print(f"My favourite programming language is: {ch}")
elif(ch==2):
    ch = "Java"
    print(f"My favourite programming language is: {ch}")
elif(ch==3):
    ch = "C#"
    print(f"My favourite programming language is: {ch}")
elif(ch==4):
    ch = "C"
    print(f"My favourite programming language is: {ch}")
else:
    print("I do not have any favourite programming language")