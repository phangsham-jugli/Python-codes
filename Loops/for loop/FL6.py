#Continue
for num in range(1,10):
    if num%3==0:
        continue
    print(f"{num}")
print("Out of loop\n")

#Break
for i in range(1,11):
    if i==8:
        break
    print(f"{i}")
print("Out of loop")
