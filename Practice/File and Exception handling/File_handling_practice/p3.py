"""
3. Count words
Read a text file and count the total number of words in it.
"""
with open("Data.txt",'tr') as fh:
    data=fh.read()
    words=data.split()

print(f"Total words:{len(words)}")