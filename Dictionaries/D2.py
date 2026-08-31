#Operation on Dictionaries
student={"Maths":80,"English":75,"Physic":72,"Hindi":60}

#to fetch marks of Maths
print(student["Maths"])

#get()
print(student.get("English"))
print(student.get("Chemistry"))
print("\n")

#membership
#in
print(80 in student)
print("English" in student)
print("\n")

#to update dict
emp1={"id":123,"name":"James","Salary":20000}
print(emp1)
print("\n")
emp1["Phone"]=987654321
print(emp1)
print("\n")

#update()
gr1={"soap":20,"cold-drink":70,"Dal":88}
print(gr1)
gr2={"soap":33,"Bread":40}
gr1.update(gr2)
print(f"The update value of item are:{gr1}")
print("\n")

#pop()
gr1.pop("Dal")
print(gr1)
print("\n")

#Working with keys and values
student1={'id':10023,'Name':"james","Marks":[23,44,55,70]}
#to fetch 44
print(student1["Marks"][1])
print("\n")

student1={'id':10023,'Name':"james","Marks":{'eng':44,'maths':60,'Phy':80}}
#to fetch physic marks
print(student1['Marks']['maths'])
print("\n")

#To fetch only keys
print(student1.keys())
print("\n")

#To fetch ony values
print(student1.values())
print("\n")

#To fetch both keys and value in pairs
print(student1.items())
print("\n")