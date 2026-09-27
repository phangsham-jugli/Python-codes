import re
"""
Find words with exactly 5 characters
Extract words whose length is exactly 5.
"""
s="Hello world Python apple mango table chair code regex laptop"
ptr=r"\b[A-Za-z]{5}\b"

re=re.findall(ptr,s)
print(re)