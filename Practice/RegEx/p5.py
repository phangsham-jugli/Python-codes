import re
"""
Find all 3-digit numbers
Extract numbers that contain exactly 3 digits.
"""
s="1234 is one two tree four and this is three digit:567 and this also 890"
pt=r"\b[\d]{3}\b"

r=re.finditer(pt,s)
for match in r:
    print(match)