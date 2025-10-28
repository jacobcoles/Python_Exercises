# === LOOP EXAMPLES ===
# Demonstrates different ways to iterate over data in Python

# === EXAMPLE 1: String iteration with enumerate ===
# Enumerate provides both index and value when iterating
cars = ["audi", "fiat", "bmw"]

#for (i, car) in enumerate(cars):
    #print(i, "__", car)  # Output: 0 __ audi, 1 __ fiat, 2 __ bmw

#print("We're at the end.")


# === EXAMPLE 2: Numeric iterations and accumulation ===
# Shows how to iterate over numbers and accumulate values
number_list = [0,1,2,3,4,5]
total_sum = 0

# Loop through list and sum all values
for num in number_list:
    total_sum = total_sum + num
#print("Total sum: ", total_sum)  # Output: 15

total_sum = 0
# Using the range function to generate numbers
for num in range(0,6):  # range(0,6) generates 0,1,2,3,4,5
    total_sum = total_sum + num
#print("Total sum using range function: ", total_sum)  # Output: 15

# === EXAMPLE 3: Modifying values during iteration ===
total_sum = 0
# Using the range function to iterate
for num in range(0,10):
    num = num*1.5  # Multiply each number by 1.5
    #print(num)

# === EXAMPLE 4: Modifying list in place with enumerate ===
number_list = [0,1,2,3]

# Use enumerate to get both index and value, then modify the list
for i, num in enumerate(number_list):
    number_list[i] = num + 1
#print(number_list)  # Output: [1, 2, 3, 4]

# === EXAMPLE 5: List comprehension ===
# List comprehension - more concise way to transform lists
number_list = [val + 1 for val in number_list]
#print(number_list)  # Output: [2, 3, 4, 5]

# === EXAMPLE 6: String list comprehension ===
cars = ["audi", "fiat", "bmw"]
cars_updated = ["Car: " + car for car in cars]
#print(cars_updated)  # Output: ['Car: audi', 'Car: fiat', 'Car: bmw']

# Normal version of above (traditional for loop approach):
cars_updated = []
for i, car in enumerate(cars):
    cars_updated.append("Car: " + car)
#print(cars_updated)

# === EXAMPLE 7: Sum calculation - manual vs built-in ===
# Manual calculation using loop
sum_value = 0
for i in range(0,11):  # 0 through 10
    sum_value = sum_value + i
#print(sum_value)  # Output: 55
# Built-in sum function (more Pythonic):
#print(sum(range(0,11)))  # Output: 55


# === EXAMPLE 8: Tuple immutability ===
# This will cause an error - tuples are immutable (cannot be modified)
some_tuple = (0, 1, 2)
for i, t in enumerate(some_tuple):
    some_tuple[i] = t + 1  # TypeError: 'tuple' object does not support item assignment
print(some_tuple)

# === EXAMPLE 9: List vs tuple syntax ===
one_item_list = [1]  # List with one item
one_item_tuple = (1 + 1)*1  # This is NOT a tuple - it's just the number 2