"""
Write a function find_largest(*numbers) that returns the largest number passed to it.
"""
def find_largest(*numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


print(find_largest(10, 25, 7, 40, 15))