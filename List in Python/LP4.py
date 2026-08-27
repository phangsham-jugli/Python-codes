n=[1,2,3,4,5,6,7,8,9,20]
#min()
print(min(n))

#max()
print(max(n))

#sum()
print(sum(n))
print("\n")

#nested lists
l1=[2,3.4,"python","java",[1,4,5,6],10]
print(l1[-2][0]) #to fetched one

l2=[[1,2],[3,4],[5,6,[7,8,9]]]
#to fetched 9
print(l2[-1])
print(l2[-1][2])

print(l2[-1][2][-1]) # to fetch 9