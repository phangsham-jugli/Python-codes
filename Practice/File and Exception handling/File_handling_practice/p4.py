"""
4. Count characters
Write a program that reads a file and counts the total number of characters, including spaces.
"""
with open("Data.txt",'tr') as fh:
    data=fh.read()

print(f"Total character are:{len(data)}")