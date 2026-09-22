fh=open("Creating_file.txt","at")
op=fh.write("\nwritten using a mode in fh5.py\n"
         "a mode use to add new content at last")
fh.close()

op=open("Creating_file.txt",'rt')
print(op.read())
op.close()

