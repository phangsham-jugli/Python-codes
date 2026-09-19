import json

"""
student={'student1':{'roll':30,'name':'john','marks':92},
         'student2':{'roll':44,'name':'jake','marks':93},
         'student3': {'roll': 60, 'name': 'Bhn', 'marks': 99} }
"""
#above is original before update() created by dump()

student={'student1':{'roll':3,'name':'john','marks':72},
         'student2':{'roll':1,'name':'jake','marks':63},
         'student3': {'roll': 2, 'name': 'Bhn', 'marks': 39} }

#Using indent in dump()
'''
#1.dump() 
with open("Practice3",'tx') as fh:
    json.dump(student,fh,indent=4)
'''
#commented the dump() cause it has already created file so running again in load() and update() it will show error

#2.load()
with open("Practice3", 'rt') as fh:
    data=json.load(fh)
    data.update(student)

#dump-the updated data again by opening file
with open("Practice3", 'tw') as fh:
    json.dump(data,fh,indent=4)


