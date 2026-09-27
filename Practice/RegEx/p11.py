import re
"""
Find all email addresses
"""
email="Contact me at abc@gmail.com or john123@yahoo.com. Invalid emails are john doe@gmail.com, test @gmail.com, and hello@ gmail.com."
ptr=r"\b[A-Za-z][\w]+[@][a-z]+[.][a-z]{2,}\b"

res=re.findall(ptr,email)
print(res)