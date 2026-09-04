#Q6. Number Divisibility Check
# Take a number and check:
# Divisible by both 3 and 5
# Divisible only by 3
# Divisible only by 5
# Not divisible by either

i=int(input("Enter a number:"))
if i%3==0 and i%5==0:
    print("Divisible both 3 and 5")
elif i%3==0 :
    print("Divisible only by 3")
elif i%5==0:
    print("Divisible only by 5")
else:
    print("Divisible by neither")