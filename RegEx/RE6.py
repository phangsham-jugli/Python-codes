import re
#Searching function
s1="Python is programming language"
phone="John-7844837583,carol-8374628426,Alice=23242424"

#match()
patt=r"[A-Z][a-z]{5}"
patt2=r"[a-z]{2}" # to match (is) but it will give none
patt3=r"\d+" # + one or

match_obj=re.match(patt,s1)
print(match_obj)

match_obj=re.match(patt2,s1)
print(match_obj)

#search ()
match_obj=re.search(patt3,phone)
print(match_obj)

#findall()
match_obj=re.findall(patt3,phone)
print(match_obj)

print("\n")

#finditer
match_obj_iter=re.finditer(patt3,phone)
print(match_obj_iter)

for matches in match_obj_iter:
    print(matches)



