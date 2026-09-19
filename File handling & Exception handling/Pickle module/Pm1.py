import pickle
students={'student1':{'roll':30,'name':'john','marks':92},
         'student2':{'roll':44,'name':'jake','marks':93},
         'student3': {'roll': 60, 'name': 'Bhn', 'marks': 99} }
with open("pickle_practice1.bin",'wb') as fh:
    for student in students:
        pickle.dump(students[student],fh)


with open("pickle_practice1.bin",'rb') as fh:
    print(pickle.load(fh))
    print(pickle.load(fh))
    print(pickle.load(fh))

