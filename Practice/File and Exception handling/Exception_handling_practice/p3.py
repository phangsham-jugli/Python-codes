"""
3. List Index
Create a list of 5 numbers and ask the user for an index. Handle the IndexError if the user enters an invalid index.
"""
l=[1,23,3,4,"Tiger"]

try:
    a=int(input("Enter the index number:"))
    num=l[a]
except IndexError:
    print("Error due to incorrect index")
else:
    print(num)
