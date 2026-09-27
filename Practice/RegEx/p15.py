import re
"""
Find words containing a dot .
"""
s="hello.world test.com python programming language.version my.file.txt example website.com"
ptr=r"\w+[.]\w+[.]\w+|\w+[.]\w+" #here i use first to search for t.t.t cause if i search for short it will not give me result

r=re.findall(ptr,s)
print(r)