# === FUNCTION EXAMPLE ===
# Demonstrates defining and using a function with return value

cars = ["toyota", "suzuki", "kia"]

# Define a function that takes a car name and formats it
def modify_car_title(car_name):
    # .title() converts string to title case (first letter capitalized)
    updated_car_title = car_name.title()
    # Add formatting characters around the title
    updated_car_title = "\n-" + updated_car_title + "."
    # Return the formatted string
    return updated_car_title

# Apply the function to each car and build a new list
cars_updated = []
for car in cars:
    updated_tile = modify_car_title(car)
    cars_updated.append(updated_tile)

print(cars_updated)  # Output: ['\n-Toyota.', '\n-Suzuki.', '\n-Kia.']
