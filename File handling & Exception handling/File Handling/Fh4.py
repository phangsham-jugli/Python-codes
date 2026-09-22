op=open("Test.txt",'rt')

#reading operation
content=op.read()
print(content)
op.close()
print(len(content))

