import re
"""
Find all uppercase letters
Extract all uppercase English letters from a string.
"""
s="THIS is for PRActic3 and to Find all thIs"
pt=r"[A-Z]+"

result=re.findall(pt,s)
print(result)