#Word Frequency Dictionary
#Given:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

nwords = ["apple", "banana", "apple", "orange", "banana", "apple"]

newdict = {}

for word in words:
    if word in newdict:
        newdict[word] += 1
    else:
        newdict[word] = 1

print(newdict)