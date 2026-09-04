#Q10. One-Line Discount Checker 🔥
amount=float(input("Enter the amount:"))

dis=amount*(10/100)
f=amount-dis
if amount >=1000:
    print(f"The final amount is with 10% discount is :{f}")
else:
    print(f"final amount is:{amount}")