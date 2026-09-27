import re
""" 
Find dates in DD-MM-YYYY format
"""
dob="Important dates are 26-09-2026, 15/08/2025, 01-01-2024, 9-12-2023, and 31-12-2026."
pt=r"\b[\d]{2}[-][\d]{2}[-][\d]{4}"

res=re.finditer(pt,dob)
for i in res:
    print(i)