
scores=[2,45,102,4,9,12,45,90,1,0,1]

#To find the sum of total scores using for loop
sm=0
for i in scores:
    sm=sm+i
print(f"the total scores is:{sm}")

#we can use this also instead of loop
print(f'{sum(scores)}\n')

#To find the highest number
highest=scores[0]

for i in scores:
    if highest < i:
        highest=i

print(f"The highest score is:{highest}")
#we can use this also instead of loop
print(f'{max(scores)}\n')

#To find the lowest
lowest=scores[0]
for i in scores:
     if lowest>i:
         lowest=i

print(f"The lowest number is: {lowest}")
#we can use this also instead of loop
print(f'{min(scores)}')

