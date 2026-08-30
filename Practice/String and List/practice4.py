numbers = [10, 20, 30, 40, 50]

# Add 60 at the end
numbers.append(60)
print(numbers)

print("\n")

# Insert 25 at index 2
numbers.insert(2,25)
print(numbers)
print("\n")

# Remove 40
numbers.remove(40)
print(numbers)
print("\n")

# Remove the last element using pop()
numbers.pop(-1)
print(numbers)
print("\n")

# Reverse the list
numbers.sort(reverse=True)
print(numbers)