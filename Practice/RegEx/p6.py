import re
"""
Find words containing only letters
Extract words that contain only A-Z or a-z.
"""
s="Hello123 world Python3 regex_test Welcome to Python programming"
pt=r"\b[A-Za-z]+\b"

res=re.findall(pt,s)
print(res)