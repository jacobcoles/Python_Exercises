# === EXAMPLE 1: Basic If/Elif/Else Statements ===
# Demonstrates conditional logic with string comparisons and nested list iteration

cars = [
        ["audi", "germany"],
        ["bmw", "germany"],
        ["fiat", "italy"],
        ["toyota", "japan"]
    ]

# Build array of car descriptions based on country of origin
car_info_array = []
for car_info in cars:
    car_brand = car_info[0]
    car_country = car_info[1]
    # Check country and categorize the car
    if car_country == "germany":
        car_info_array.append("Best car is " + car_brand)
    elif car_country == "italy":
        car_info_array.append("Completely adequate car is " + car_brand)
    elif car_country == "japan":
        car_info_array.append("Completely reliable car is " + car_brand)
    else:
        car_info_array.append("No opinion on " + car_brand)

# Build final output string by concatenating all descriptions
final_output_string = "The car info is as follows:\n\n"

for a in car_info_array:
    final_output_string = final_output_string + a + "\n"
#print(final_output_string)



# === EXAMPLE 2: Boolean OR Operator ===
# Demonstrates 'or' - returns True if at least one condition is True

guessed_number = 20

# Check if number is greater than 5 OR less than 20
if (guessed_number > 5 or guessed_number < 20):
    print("In range!")
else:
    print("Out of range!")


# === EXAMPLE 3: Boolean AND Operator ===
# Demonstrates 'and' - returns True only if BOTH conditions are True
# Also shows combining multiple conditions in if/elif statements

cars = [
        ["audi", "germany", 2],
        ["bmw", "germany", 15],
        ["fiat", "italy", 19],
        ["toyota", "japan", 20]
    ]

car_info_array = []
for car_info in cars:
    car_brand = car_info[0]
    car_country = car_info[1]
    car_sales = car_info[2]
    # Using 'and' to check both country AND sales criteria
    if car_country == "germany" and car_sales > 5:
        car_info_array.append("Best car is " + car_brand)
    elif car_country == "germany" and car_sales <= 5:
        car_info_array.append("Worst car is " + car_brand)
    elif car_country == "italy":
        car_info_array.append("Completely adequate car is " + car_brand)
    elif car_country == "japan":
        car_info_array.append("Completely reliable car is " + car_brand)
    else:
        car_info_array.append("No opinion on " + car_brand)

final_output_string = "The car info is as follows:\n\n"