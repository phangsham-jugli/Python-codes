import re

#Sub()
s1="Sunday,Monday,Tuesday,Monday,Sunday,Saturday"
patt=r"S[a-z]+"
replacement="Friday"

result=re.sub(patt,replacement,s1)
print(result)
print("\n")

#example 2
message=("We are learning Python RE,Using re we can search for a pattern in a given srtring,using the sub(),we can replace the "
         "pattern with a given string.")
patt=r"\bre\b" #we are using \b cause it will change are also cause it has re ,it is called word boundary
replacement="Regular Expression"

result=re.sub(patt,replacement,message,flags=re.IGNORECASE) #flags= is use to ignore cases in re and RE
print(result)
print("\n")

#example 3
Phone_num="+91-938472642,+91-485736362"
patt=r"[+-]"
replacement=""
result=re.sub(patt,replacement,Phone_num)
print(result)