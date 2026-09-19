import pickle
students={'student1':{'roll':30,'name':'john','marks':92},
         'student2':{'roll':44,'name':'jake','marks':73},
         'student3': {'roll': 60, 'name': 'Bhn', 'marks': 89} }
with open("pickle_practice2.bin",'wb') as fh:
    for student in students:
        pickle.dump(students[student],fh)


with open("pickle_practice2.bin",'rb') as fh:
    while True:
        try:
            data=pickle.load(fh)
            print(data)
        except EOFError:
            print("done")
            break

#to print only who score above 90
with open("pickle_practice2.bin",'rb') as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['marks']>=90:
                print(data['name'])
        except EOFError:
            print("done")
            break