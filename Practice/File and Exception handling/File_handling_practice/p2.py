"""
2. Count lines
Write a program to open data.txt and count how many lines are present in the file.
"""
with open("Data.txt","tr") as fh:
     data=fh.readlines()


print(len(data))