# Count a word
# Given:

sentence = "python is easy and python is powerful and python is popular"

# Find:

# How many times "python" occurs
# Replace "python" with "Python"
# Convert the sentence into a list of words

p=sentence.count("python")
print("the total occurance of python is:",p)
print("\n")
r=sentence.replace("python","Python")
print(r)

words=sentence.split()
print(words)