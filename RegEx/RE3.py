import re
"""Special character in python"""

#1.r
s1="This is python and for regular expression,and the current version is python3.13"
pat=r"[A-Z][a-z]"
match=re.search(pat,s1)
print(match)

#2.\d
pat=r"[a-z][a-z][a-z]\d"
match=re.search(pat,s1)
print(match)

#3.\D
pat=r"[a-z][a-z][a-z][a-z]\D"
match=re.search(pat,s1)
print(match)

s2="""hii these
is learning special character in 
regex"""

#4.\s
pat=r"[a-z][a-z][a-z][a-z]\s"
match=re.search(pat,s2)
print(match)

#5.\S
pat=r"[a-z][a-z][a-z]\S"
match=re.search(pat,s2)
print(match)

#6.\w
pat=r"[a-z][a-z][a-z][a-z]\w"
match=re.search(pat,s2)
print(match)

#7.\W
pat=r"[a-z][a-z][a-z][a-z]\W"
match=re.search(pat,s2)
print(match)