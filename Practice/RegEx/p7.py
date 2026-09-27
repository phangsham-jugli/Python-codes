import re
"""
Find words starting with a capital letter
"""
s="Hello my Friend and Python are Great for Learning Regex"
pt=r"[A-Z][a-z]+"

res=re.findall(pt,s)
print(res)