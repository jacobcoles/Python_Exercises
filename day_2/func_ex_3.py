# === FUNCTION WITH LIST COPYING ===
# Demonstrates working with list copies to avoid modifying the original

cars = ["toyota", "suzuki", "kia"]

# Function that creates a copy of the list before modifying it
def modify_list(car_list):
    # car_list[:] creates a copy of the list (not just a reference)
    car_list_copy = car_list[:]
    # Modify the copy, not the original
    car_list_copy.append("new car")
    return car_list_copy

# Call the function with the original list
output_result = modify_list(cars)

# Output shows the modified copy
print(output_result)  # Output: ['toyota', 'suzuki', 'kia', 'new car']
# Original list remains unchanged
print(cars)  # Output: ['toyota', 'suzuki', 'kia']