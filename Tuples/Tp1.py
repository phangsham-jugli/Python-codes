#tuple
t1=("Python",10,2.3,4,True,(5,6),[1,55,66])
print(len(t1))

print(t1[0])
print(t1[-1])

#slicing tuple
n=t1[0:-2:1]
print(f"{n}\n")
n2=t1[0:8:2]
print(f"{n2}\n")

#list to tuple
l1=[1,2,3,4,5]
print(f"{l1}\n")
print(type(l1))

t2=tuple(l1)

print(f"{type(t2)}\n")
print(f"{t2}\n")

#tuple to list
l2=list(t1)
print(f"{l2}\n")
print(f"{type(l2)}\n")


#operation in tuple
#1.concatenation
s1=(1000,"Mark")
s2=(54.6,44.3,66)
s3=s1+s2
print(f"{s3}\n")

#2.repetition
print(f"{s1*3}\n")

#3.Membership
# in
print("Mark" in s1)
#not in
print(54.6 not in s2)

#count()
print(f"\n{s1.count("Mark")}\n")
print(f"{s2.count(66)}\n")

# s="tiger"
# print(s.count("i"))
# -above is to count element of string

#index()
print(f"{s3.index(44.3)}\n")
print(f"{s1.index(1000)}\n")

tp=(10,1,2,3,1)
print(f"{tp.index(1)}\n")
#it will give the index number 1 cause it give first occurrence index number

#min()
print(f"{min(tp)}\n")
#max()
print(f"{max(tp)}\n")
#sum()
print(f"{sum(tp)}\n")
