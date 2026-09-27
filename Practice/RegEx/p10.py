import re
"""
Find words starting with Th
Find words such as The, This, That, etc.
"""
s="The teacher said This is a simple Thing that we can learn Through practice."
pt=r"\b[Th][a-z]+\b"

r=re.finditer(pt,s)
for matches in r:
    print(matches)
