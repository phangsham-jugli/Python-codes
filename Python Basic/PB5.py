# Associativity & Precedence of operators
sum=5+20*10
print(sum) #bodmas rule but when there is division associativity rule from left to right side

#---------------------------------------
name="Mark"
age=30
tf=name=="Mark" or name=="John" and age<18
print(tf) #(first priority is and)

jf=(name=="Mark" or name=="John") and age<18
print(jf) #bracket has highest priority than and ,or

ex=2**1**3 #associativity is from right to let
print(ex)