 #Nested loop
for i in range(3):
    for j in range(2):
        print(f"i={i},j={j}\n")

print("\n")

#Printing multiplication table from 1 to 10

for i in range(1,11):
    print("Multiplication table of ", i)
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print("\n")