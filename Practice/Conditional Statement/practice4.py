#Q4. Electricity Bill ⭐
unit=float(input("Enter the electricity-1 unit:"))
if unit >=0:
    if unit <= 100 and unit >= 0:
        bill = unit * 5
        print("Your bill is:",bill)
    elif unit <= 200 and unit >= 101:
        bill = unit * 7
        print("Your bill is:",bill)
    elif unit <= 300 and unit >= 201:
        bill = unit * 10
        print("Your bill is:",bill)
    else:
        bill = unit
        print("Your bill is:",bill)
else:
    print("invalid unit")