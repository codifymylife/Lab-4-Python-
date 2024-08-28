mark = float(input("Enter your mark: "))

#condition
if mark >=80 and mark <= 100:
    grade = "A"
elif mark >=60 and mark <= 79:
    grade = "B"
elif mark >= 40 and mark <= 50:
    grade = "C"
elif mark>=0 and mark <= 39:
    grade = "F"
else:
    print("Undefined")

if(mark >=0 and mark <=100):
    print(f"Grade: {grade}")