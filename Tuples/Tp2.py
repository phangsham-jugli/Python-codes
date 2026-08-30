#immutable
s1="Python is fun to learn"
print(s1.replace("Python","Guava"))
print(f"{s1}\n")
#here original value does not change only replace

# t=("mango","apple","banana")
# t1.append("orange") -this shows error cause we cannot change tuple elements
# print(t1)

#Mutable
l=["apple","banana","mango"]
print(id(l)) #before change memory location
l.insert(3,"Guava") #change original value/create new memory location
print(l)
print(id(l)) #after change in memory location
print("\n")

#changing using index number
l[2]="Orange"
print(l)
print(id(l)) #new memory location

#CANNOT CHANGE THE STRING AND TUPLES