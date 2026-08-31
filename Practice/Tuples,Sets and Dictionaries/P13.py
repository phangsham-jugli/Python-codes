#Remove Duplicates using sets
#Given:
numbers = [10, 20, 10, 30, 20, 40, 30, 50, 40]

# convert the list into a set to remove duplicate values.
# Then convert the set back into a list.

#using typecasting converting into sets
st=set(numbers)
print(st)

#using typecasting converting into list
l=list(st)
print(l)