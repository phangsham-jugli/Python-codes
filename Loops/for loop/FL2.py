#for loops with String
S1="Hello World"

for char in S1:
    print(char)

print("End of loop with string \n") #outside the loop

#for loop in tuples
t1=(1,2,3,'Tea',"Ice","Orange")
for e in t1:
    print(f'{e}')

print("End of loop with tuple\n") #outside the loop

#for loop with dictionaries
employee={"id":1023,"Name":"John","Department":"Managing"}
for i in employee.items():
    print(i[0],i[1])

print("End of loop with dict\n")  # outside the loop