import re
"""
Find all lowercase letters
Extract all lowercase English letters from a string.
"""
s="This is the string from python version3.13 and practice 2"
ptt=r"[a-z]+"

result2=re.findall(ptt,s)
print(result2)