# === IMPORTING AND USING MODULES ===
# Demonstrates how to import functions from custom modules

# Import all functions from pizza_module.py using wildcard (*)
from pizza_module import *

# Call the imported make_pizza function
output = make_pizza(10, "fish")
make_pizza()  # This will cause an error - missing required 'size' argument

# Print the result
print(output)  # Output: "The pizza is 10 inches and has toppings fish."