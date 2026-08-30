#Sets
s1={"Apple",20,40}
print(s1)
print(len(s1))
print(type(s1))
print("\n")
#Basic operation on sets
#Membership
#in
s={1,2,3,4,0,-1,-2}
print(-1 in s)
print(2 in s)
print(6 in s)
print("\n")

#not in
print(3 not in s)
print(7 not in s)
print("\n")

#converting tuple,list into sets vice versa
T=tuple(s1)
print(T)
print(type(T))
print("\n")

l=list(s1)
print(l)
print(type(l))
print("\n")

t1=("Mango",1,2)
print(type(t1))
S=set(t1)
print(S)
print(type(S))
print("\n")

l2=["Orange",5,6]
print(type(l2))
S2=set(l2)
print(S2)
print(type(S2))
print("\n")

#add()
S2.add("Lion")
print(S2)
print("\n")

#remove()
S2.remove("Orange")
print(S2)
print("\n")

#discard()
S2.discard(10)
print(S2)
S2.discard(5)
print(S2)
print("\n")

#OPERATION ON SETS
student1={"maths","English","History","French","Science"}
student2={"physics","chemistry","history","arithmetic","English"}
student3={"maths","English","History","French","Science"}

#1.intersection
common=student1 & student2,student3
print(common)
print("\n")

#2.Union
Together=student1 | student2 | student3
print(Together)
print("\n")

#3.Difference
days={"Mon","Tue","Wed","Thur","Fri","Sat","Sun"}
weekend={"Sat","Sun"}
D=days - weekend
print(f"Days which are not in weekend are:{D}\n")


#Frozen Sets
fs1=frozenset({1,2,3,4,5})
print(fs1)
print(type(fs1))
print("\n")
fs2=frozenset({3,4,6,2,7,9,0})
print(fs2)
print(type(fs2))
print("\n")

#union
All=fs1 | fs2
print(All)
print("\n")

#intersection
cm=fs1.intersection(fs2)
print(cm)
print("\n")

#difference
dff=fs1.difference(fs2)
print(dff)

