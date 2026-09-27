import re
"""
Find phone numbers
"""
ph="Contact: 9876543210, 8123456789, 7654321098, 6123456789. Invalid numbers: 5123456789, 1234567890, 987654321."
pt=r"\b[9876][\d]{9}\b"

res=re.finditer(pt,ph)
for i in res:
    print(i)