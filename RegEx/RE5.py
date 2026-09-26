import re
s1="Python is programming language"

# ^ -Caret
patr=r"^[a-z]{7}"
match_obj=re.search(patr,s1)

print(match_obj)


# $
patr=r"[a-z]{7}$"
match_obj=re.search(patr,s1)

print(match_obj)

# group- ()
email="abc-123@gggmail.com and character .1234gjej.edu"
ptt=r"(com|edu)"
match_obj=re.search(ptt,email)

print(match_obj)



