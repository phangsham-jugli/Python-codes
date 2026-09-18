#Else block
try:
    with open("Notes.txt","tr") as eh:
        data=eh.read()

except FileNotFoundError as err:
    print("File not found")
    print(err)

else:
    print(data)