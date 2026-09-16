"""
filter() + lambda
Given:

words = ["apple", "cat", "banana", "dog", "elephant"]

Find words having more than 5 characters.
"""
words = ["apple", "cat", "banana", "dog", "elephant"]

fun=lambda x:True if len(x)>5 else False

check=filter(fun,words)

print(list(check))