# === PIZZA MODULE ===
# This module contains reusable pizza-related functions
# Can be imported into other Python scripts

def make_pizza(size, *toppings):
    """
    Creates a formatted string describing a pizza.

    Args:
        size: Pizza size in inches
        *toppings: Variable number of topping names

    Returns:
        Formatted string describing the pizza
    """
    output_string_template = "The pizza is " + str(size) + " inches and has toppings "
    for topping in toppings:
        output_string_template = output_string_template + " " + topping + ","
    output_string_template = output_string_template.strip(",") + "."
    return output_string_template

def function_2():
    """Placeholder function for demonstration."""
    pass