import re
"""
Find all .com websitesa
"""
website="Visit google.com and github.com for more information. You can also check example.org and python.org."
ptr=r"\b[\w]+[.]com\b"

r=re.findall(ptr,website)
print(r)