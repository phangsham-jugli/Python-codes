import re
#Quantifiers
message="The current Python version is 3.13 other previous version  are 3.12,3,11,3.10"

# +
pat=r"[A-Z][a-z]+"
match_obj=re.search(pat,message)
print(match_obj)

pat2=r"[a-z]+"
match_obj=re.search(pat2,message)
print(match_obj)


# ?
pat3=r"[A-Z][a-z]?"
match_obj=re.search(pat3,message)
print(match_obj)

pat4=r"[a-z]?"
match_obj=re.search(pat4,message)
print(match_obj)

# *
pat5=r"[A-Z][a-z]*"
match_obj=re.search(pat5,message)
print(match_obj)

pat6=r"[a-z]*"
match_obj=re.search(pat6,message)
print(match_obj)


#{n}
par=r"[a-z]{4}"
match_obj=re.search(par,message)
print(match_obj)

par2= r"[A-Z][a-z]{4}"
match_obj=re.search(par2,message)
print(match_obj)

par3= r"[a-z]{3,4}"
match_obj=re.search(par3,message)
print(match_obj)

