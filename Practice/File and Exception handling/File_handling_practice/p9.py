"""
9. Count vowels
Read a text file and count how many vowels (a, e, i, o, u) are present.
"""
with open("Data.txt",'tr') as fh:
    data=fh.read()

count=0

for i in data:
    if i =='a' or i =='i' or i =='e' or i== 'o' or i== 'u':
        count+=1


if count==0:
    print("Does not contain vowel")
else:
    print(f"There are {count} in Data")