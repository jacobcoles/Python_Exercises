# === FUNCTION WITH *ARGS (ARBITRARY ARGUMENTS) ===
# Demonstrates using *args to accept any number of positional arguments

# === EXAMPLE 1: Function with only *args ===
def make_pizza(*toppings):
    # *toppings accepts any number of arguments as a tuple
    output_string_template = "The pizza has toppings "
    for topping in toppings:
        output_string_template = output_string_template + " " + topping + ","
    #print("The pizza has toppings ", topping1, topping2, topping3)
    # .strip(",") removes trailing comma
    output_string_template = output_string_template.strip(",") + "."
    return output_string_template

output_string = make_pizza("mushroom", "pineapple")
#print(output_string)  # Output: "The pizza has toppings mushroom, pineapple."


# === EXAMPLE 2: Function with required argument and *args ===
# Function with fixed 'size' parameter followed by variable toppings
def make_pizza(size, *toppings):
    output_string_template = "The pizza is " + str(size) + " inches and has toppings "
    for topping in toppings:
        output_string_template = output_string_template + " " + topping + ","
    #print("The pizza has toppings ", topping1, topping2, topping3)
    output_string_template = output_string_template.strip(",") + "."
    return output_string_template


# === EXAMPLE 3: Unpacking a list with * operator ===
pizzas = [
    ("cheese", 12, ["cheese", "oil"]),
    ("margarita", 4, ["cheese", "tomato"])
]

for p in pizzas:
    #name = p[0]
    size = p[1]
    ingredients = p[2]  # list of toppings
    # *ingredients unpacks the list into separate positional arguments
    make_pizza(size, *ingredients)

output_string = make_pizza(12, "mushroom", "pineapple")
print(output_string)  # Output: "The pizza is 12 inches and has toppings mushroom, pineapple."

