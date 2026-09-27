import re
"""
Find all digits
Given a string, find every digit present in it.
"""
s="This 1 practice and i am learning to extract the number 6452874"
ptt=r"\d+"
result=re.findall(ptt,s)
print(result)
print("\n")

match_obj=re.finditer(ptt,s)
for matches in match_obj:
    print(matches)