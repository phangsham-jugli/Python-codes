#Q.8 BMI Calculator
weight = float(input("Enter your weight:"))
Height = float(input("Enter your height in meter:"))
BMI = weight / (Height ** 2)

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 24.9:
    print("Normal")
elif BMI >= 25 and BMI < 29.9:
    print("Overweight")
else:
    print("Obese")