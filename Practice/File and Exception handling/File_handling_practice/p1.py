"""
1. Read a file
Create a file data.txt containing some text. Write a Python program to:
- Open the file in read mode.
- Read the entire content.
- Print it.
"""
with open("Data.txt",'rt') as fh:
    data=fh.read()

print(data)