#Dictionary Add and Delete
# Given:
car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2024
}

# Perform:
# Add "color": "Black"
# Change the year to 2025
# Delete "model"
# Print the final dictionary

car["color"]="Black"
car["year"]=2025
car.pop("model")
print(car)