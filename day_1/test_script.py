# === BASIC PYTHON EXAMPLES ===
# Demonstrates imports, variable assignment, type checking, and print formatting

# Import the math module to use mathematical functions
import math

# Using math.exp() to calculate e^10
exponentiated = math.exp(10)

# Multiple variable assignment in one line
number, number_2 = 1000000, 0.9

# Print statement with multiple arguments (automatically adds spaces)
# Demonstrates the type() function to check data types
print("The type for number ",
      number,
      " is ",
      type(number),  # Returns <class 'int'>
      "\n\n",
      "The type for the other number ",
      number_2,
      " is ",
      type(number_2)  # Returns <class 'float'>
      )

print("Exponentiated: ", exponentiated)