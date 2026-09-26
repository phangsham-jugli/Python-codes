#Regex exercise
import re

ptr=r"\b[a-zA-Z]+[\w_.-]+[@][a-z]+[.][a-z]+\b"

with open("E:\\Ai Engineer Course\\PythonProject\\RegEx\\Student_details","rt") as fh: # i use \\ to represent \Ai cause python do not detect direct /Ai
    data=fh.read()


match_obj=re.finditer(ptr,data)

for matches in match_obj:
    print(matches)
