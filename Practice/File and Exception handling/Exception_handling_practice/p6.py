"""
6.Try–Except–Finally
Write a program that opens a file and reads its contents. Use finally to display "Program execution completed" whether an exception occurs or not.
"""
try:
    l = [2, 3, 4, 5]
    num=l[4]
    print(num)
except Exception as ex:
    print(ex)
finally:
    print("Completed!")
