import copy
#Shallow copy
l1=[11,22,["Punks",33,1],8]
l2=copy.copy(l1)
print(f'Before: l1-> {l1}',id(l1))
print(f'Before: l2-> {l2}',id(l2))
print("\n")

l1[0]=69 #this will not change in l2
l1[2][0]="tiger"  # this will change both l1 and l2 even though it is done in l1 because due to inner location
print(f'l1-> {l1}',id(l1))
print(f'l2-> {l2}',id(l2))
print("\n")

#Deep copy
l2=copy.deepcopy(l1)
l1[0]=69 #this will not change in l2
l1[2][0]="tiger"  # this will now not change l2
print(f'l1-> {l1}',id(l1))
print(f'l2-> {l2}',id(l2))