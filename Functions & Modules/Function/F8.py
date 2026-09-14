#Lambda function
fun=lambda a,b:a+b
rest=fun(2,3)
print(rest)

#filter() and map() with Lambda
#1.filter()
seq=[1,2,3,4,5]
result=filter(lambda x:True if x%2!=0 else False,seq)
print(list(result))

#2.map()
seq2=[2,4,6,8]
result2=map(lambda x:x**2,seq2)
print(list(result2))
