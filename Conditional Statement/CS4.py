#nested statement
x=int(input("Did you pass your exams yes=1/no=0:"))

if x==1:
    marks=float(input("Enter your marks:"))
    if marks>=45:
        if marks >= 90:
            print("Grade:A+")
        elif marks >= 80:
            print("Grade:A")
        elif marks >= 75:
            print("Grade:B+")
        elif marks >= 60:
            print("Grade:B")
        else:
            print("Grade:C")
    else:
        print("Your mf Shameless person!")
else:
    print("Shame on you ,your are a failure:")
