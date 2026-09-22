"""
8. Copy a file
Read the contents of source.txt and create another file called backup.txt containing exactly the same content.
"""
with open("Student.txt",'tr') as fh:
    data=fh.read()

with open("Backup.txt",'tx') as nfh:
    nfh.write(data)