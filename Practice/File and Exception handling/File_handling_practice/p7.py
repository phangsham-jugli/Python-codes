"""
7. Find a word
Read data.txt and ask the user to enter a word. Check whether that word exists in the file.
"""
word=input("Enter the word:")
with open("Data.txt",'tr') as fh:
    data=fh.read()

if word in data:
    print(f"{word} is present in data")
else:
    print(f"{word} not present")