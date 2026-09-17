#With Statement
"""Example1"""
with open("Test.txt","tr") as fh:
     content=fh.read()

print(content)

#Example 2
with open("Test2.txt","tw") as new:
    new.write("Created using with statement in fh6\n")


#Example3
with open("Test2.txt",'rt') as t2:
    new2=t2.read()

print(new2)



