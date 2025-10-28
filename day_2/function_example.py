# === FUNCTION WITH DOCSTRING AND MULTIPLE RETURN VALUES ===
# Demonstrates function documentation and returning multiple values

def generate_output_string(age, lastname):
    """
    This function outputs a string describing an individual.
    Args:
    - Age: The person's age (integer)
    - lastname: The person's last name (string)

    Returns:
     - output_string: A formatted greeting with name and age
     - A second string value
    """
    # Build greeting string with name and age
    output_string = "Hello " + lastname + "\nYour age is " + str(age)
    # Functions can return multiple values as a tuple
    return output_string, "output2"

# Unpack multiple return values into separate variables
output, output2 = generate_output_string(20, "Smith")