#Set Union Intersection
#Given:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Find:
# Union
# Intersection
# Elements only in A
# Elements only in B

U=A.union(B)
print(U)
#alternative-
#U=A|B
print("\n")

I=A & B
print(I)
#Alternative-
#I=A.intersection(B)
print("\n")

EA=A-B
print(f"Elements only in A:{EA}\n")

EB=B-A
print(f"Elements only in B:{EB}\n")
