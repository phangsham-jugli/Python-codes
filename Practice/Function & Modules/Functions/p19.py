"""
map() + lambda
Convert this list of temperatures from Celsius to Fahrenheit:

celsius = [0, 10, 20, 30, 40]
"""
celsius=[0,10,20,30,40]
fun=lambda x:(x*9/5)+32

fahrenheit=map(fun,celsius)

print(list(fahrenheit))