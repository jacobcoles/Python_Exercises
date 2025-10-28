# === DICTIONARY EXAMPLES ===
# Demonstrates dictionary operations and methods in Python

# === EXAMPLE 1: Basic dictionary and .keys() method ===
alien = {"colour": "green", "height": 12}

# .keys() - returns all dictionary keys as a dict_keys object
#print(list(alien.keys()))  # Output: ['colour', 'height']


# === EXAMPLE 2: Dictionary methods - keys() and values() ===
companies_head_count = {"ABC": 200, "DEF": 210}

# .keys() - get all keys
#print(list(companies_head_count.keys()))  # Output: ['ABC', 'DEF']

# .values() - get all values
#print(list(companies_head_count.values()))  # Output: [200, 210]

# === EXAMPLE 3: Nested dictionaries and .items() method ===
# Dictionary containing dictionaries (nested structure)
head_count = {"TL": {
                "Switzerland": 500,
                "Netherlands": 500
                },
               "Tetra Pak": {
                "Switzerland": 300,
                "Netherlands": 600
                }
              }

# .items() - returns key-value pairs as tuples
print(head_count.items())

# Iterate through nested dictionary and calculate totals
for company_name, company_count_per_country in head_count.items():
    total = 0
    # Sum all country counts for each company
    for count in company_count_per_country.values():
        total = total + count
    # f-string formatting for output
    print(f"Amount for {company_name} is {str(total)}")

