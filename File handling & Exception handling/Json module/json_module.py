import  json
#1.dump()/without indent
l1=[1,2,3,"hello"]

with open("Practice2", "tw") as fh:
    json.dump(l1,fh)
