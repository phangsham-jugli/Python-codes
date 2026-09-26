import re

from RegEx.RE7 import Phone_num

#Compile()
phone="Alice-9183748274,Mark-9847347364,Carol-8274628475"

#can be used in other datatype also like in Example 2
pattern=r"\d{10}"
pattern_compiled=re.compile(pattern)

match_obj=re.findall(pattern_compiled,phone)
print(match_obj)
print("\n")

#Example 2 //converting txt file into string and finding phone number
with open("Student_details",'rt') as fh:
    data=fh.read()

phone_num=re.finditer(pattern_compiled,data) #we can use findall also

for match in phone_num:
    print(match)
