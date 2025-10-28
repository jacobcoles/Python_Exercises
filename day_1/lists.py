# === LIST OPERATIONS EXAMPLES ===
# Demonstrates various ways to manipulate and work with Python lists

# Create a basic list
bikes = ['mountainbike', "cannondale", "cannondale", "road"]

# Replace - modify list element by index
bikes[0] = "Some new thing"
#print(bikes)  # Output: ['Some new thing', 'cannondale', 'cannondale', 'road', 'New bike']

# Append - add element to end of list
bikes.append("New bike")
#print(bikes)

# Lists within lists - nested list structure
bikes_updated = [["ducati"], ["hyundai", "fiat", "toyota"]]
#print(bikes_updated)

# Insert - add element at specific index position
bikes.insert(1, "ducati")
#print(bikes)

# Delete - remove element by index
del bikes[0]
#print(bikes)

# Popping - remove and return last element (or at specific index)
#specific_bike = bikes[-1]
#del bikes[-1]
# Same as above but in one operation:
#specific_bike = bikes.pop(-1)

#print("Pre removal: ", bikes)

# Remove - delete first occurrence of a specific value
bikes.remove("cannondale")  # Removes first "cannondale" only
#print("Post removal: ", bikes)

# Sorting - sort list in place
cars = ["bmw", "audi", "fiat", "toyota"]
#print(cars)
cars.sort(reverse=True)  # Sort in descending order
#print(cars)

# Slice syntax - extract portions of a list
cars_subset = cars[0:3]      # Get elements from index 0 to 2 (3 is exclusive)
cars_copy = cars[:]          # Create a copy of entire list
cars_flipped = cars[::-1]    # Reverse the list

# Finding the length of a list - returns number of elements
print(len(cars))

