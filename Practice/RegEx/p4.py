import re
"""
Find all words starting with A or a
From a sentence, find every word whose first character is A or a.
"""
s="This is A apple An a boy And a car"
pt=r"\b[Aa]+"

result=re.finditer(pt,s)
for match in result:
    print(match)