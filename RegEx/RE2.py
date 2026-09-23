import re
#Search using pattern

s1="Python is very much advanced and it has 3.13,3.12,3.14 version"
src=re.search("[0-9][0-9]",s1)
print(src)

src2=re.search("[0-9][0-9][0-9]","House number 123/A")
print(src2)

#.
src=re.search("[0-9].[0-9][0-9]",s1)
print(src)

src=re.search("[0-9].[0-9]",s1)
print(src)

src=re.search("[0-9].[0-9]","House number 123/A")
print(src)

#[.]
src2=re.search("[0-9][.][0-9][0-9]","House number 123/A")
print(src2)