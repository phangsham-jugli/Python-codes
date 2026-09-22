"""
Student Marks Validation ⭐
Write a program that takes a student's marks as input.
- If marks are not a number → handle ValueError
- If marks are less than 0 or greater than 100 → use raise ValueError
- Otherwise, display "Valid marks"
- Use finally to display "Validation completed".
"""
try:
    marks=int(input("Enter the marks:"))

    if marks<0 or marks>100:
       raise Exception("Error")

except ValueError as er:
    print(er)
else:
    print("valid marks")
finally:
    print("Validation completed!")



