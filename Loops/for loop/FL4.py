#range()
#range(start)-->default value 0
#range(step)-->default value 1

#To generate index
groceries=["Milk","Biscuit","Sugar"]
for i in range(len(groceries)): #we can also use range(3)
    print(i)

#to print profit of quater 1 to 4
profit=[9,6,7,2]
for p in range(len(profit)): #this will generate index
    q=p+1
    print(f"Profit of quater {q} is:{profit[p]}")
    #profit[p] = to run each element in profit

