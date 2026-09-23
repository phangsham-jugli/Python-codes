import re
s1="Python is very much advanced and it has 3.13,3.12,3.14 version"

serc=re.search("13",s1)
print(serc)

if re.search("13",s1):
    print("Found!")
else:
    print("Not found")

print(s1[42:44:1])