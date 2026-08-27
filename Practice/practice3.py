# Use string methods to:
# Remove the extra spaces
# Replace "easy" with "powerful"
# Check whether "Python" is present
# Count the number of "e" characters

text = "  Python is easy to learn  "
print(text)

newtxt=text.strip()
print(newtxt)
print("\n")

print("Python" in text)
print("\n")

c=text.count("e")
print(c)