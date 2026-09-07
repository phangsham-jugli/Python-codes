#To print multiplication table from 1 to 10

for i in range(1,11):
    print("Multiplication table of ",i)
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        
    print("\n")