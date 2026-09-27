import re
"""
Find numbers between 10 and 99
Extract all two-digit numbers from a string.
"""
str="I have 5 apples, 25 oranges, 103 bananas, 67 mangoes, 8 grapes, and 99 lemons."
ptr=(r"\b[\d]"
     r"{2}\b")
res=re.findall(ptr,str)
print(res)