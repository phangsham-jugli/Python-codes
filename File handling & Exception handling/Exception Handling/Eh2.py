try:
    with open("practicefile.txt","tr") as eh:
        data=eh.read()

    print(data)
except FileNotFoundError as err:
    print("File not found")
    print(err)

