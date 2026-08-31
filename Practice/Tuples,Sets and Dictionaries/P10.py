#Dictionary Methods
#Given:
product = {
    "name": "Laptop",
    "price": 55000,
    "brand": "HP"
}

# Use dictionary methods to print:
# All keys
# All values
# All key-value pairs
# Check whether "price" exists

print(f"All the keys are:{product.keys()}\n")
print(f"All the values are:{product.values()}\n")
print(f"All the pairs of keys and values are:{product.items()}\n")
print(product.get("price"))