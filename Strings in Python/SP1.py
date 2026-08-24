#Slicing in Strings
s1="hello world"
print(s1[1:8:1])
print(s1[2:8:2])
print(s1[0:11:1]) #length of s1 is 10 bt we keep 11 cause end is excluded
print("\n")

#Fstring
name="john"
age=23
language="Python"
hours=3

#john is 23 years old .he studies python 3 hour a day
print(name,"is",age,"years old.He studies",language,hours,"a day")

#using-fstring
print(f"{name} is {age} years old and he studies {language} {hours} a day \n")

print("for showing double quoted text we should use backslash \"like this\" \n")

# 4.Operation on strings
# *
s1="string "
print(s1*3)

#Membership
#in
s1="python"
print("p" in s1)
print("o" in s1)
print("z" in s1)

#not in
print("java" not in s1)
print("p" not in s1)

# *comparison of String
print("python"=="python")
print("python "=="python")

#Strip()
s1="String "
print(s1.strip()=="String")

print("\n")
#replace()-does not change original value/String
s1="we are learning Python"
print(s1.replace("Python","java"))
print(s1)

#to replace only one letter
print(s1.replace("e","E",1))
print(s1.replace("n","T",2))

#count()
s1="hello my name is pj from dj"
s2="j"
print(f"\noccurrences of j is {s1.count(s2)}")
s3="ll"
print(f"occurrences of ll is {s3.count(s2)}\n")

#cases
#1.upper()
s="Mark is a good BOY"
print(s.upper())
#2.lower()
print(s.lower())
#3.title
print(s.title())
#4.capitalize
print(s.capitalize())

print("\n")

#startswith()
print(s.startswith("Mark"))
print(s.startswith("B"))
print(s.startswith("BOY"))
print("\n")
#endswith()
print(s.endswith("Z"))
print(s.endswith("BOY"))
print(s.endswith("Y"))