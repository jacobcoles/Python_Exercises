# === FILE PATHS AND FILE OPERATIONS ===
# Demonstrates working with file paths, reading, writing, and exception handling

# === EXAMPLE 1: Basic file reading with pathlib ===
from pathlib import Path

#path = Path("files/text.txt")  # Create a Path object

#contents = path.read_text()  # Read entire file content as string

#print(contents)


# === EXAMPLE 2: Working with current directory ===
import os
#print("Current directory: ", os.getcwd())  # Get current working directory


# === EXAMPLE 3: String splitting ===
#print("hello there".split())  # Split string by whitespace --> ['hello', 'there']

#print("hello there".split()[-1])  # Get last element --> 'there'

# === EXAMPLE 4: Parsing file paths using string split ===
example_path = "/User/directory/text.txt"
#print(example_path.split("/"))  # Split path into parts

split_path = example_path.split("/")
file_name = split_path[-1]  # Get filename (last element)
#print(file_name)  # Output: 'text.txt'

parent_directory = split_path[-2]  # Get parent directory name
#print(parent_directory)  # Output: 'directory'

# === EXAMPLE 5: Conditional path handling ===
# Use current working directory instead:
current_working_dir = os.getcwd()
#print(current_working_dir)

split_path = current_working_dir.split("/")
current_folder = split_path[-1]  # Get current folder name
#print(current_folder)

# Check if we're in the correct directory
if current_folder == "day_2":
    # make the path refer to the correct folder, fix the path
    pass
else:
    # don't do anything
    pass

# ------

# === EXAMPLE 6: Reading file line by line ===
path = Path("files/text.txt")

contents = path.read_text()  # Read entire file

lines = contents.splitlines()  # Split content into list of lines

# Enumerate to get both line number and content
for i, l in enumerate(lines):
    print("Line number: ", i, ", Line: ", l)

# === EXAMPLE 7: Writing to files ===
save_path = Path("files/text_2.txt")
# write_text() writes string to file (creates or overwrites)
save_path.write_text("Hi there, I love python!")

# === EXAMPLE 8: Exception handling with try/except ===
# Demonstrates catching specific errors when working with files

try:
    # Try to execute this code block
    read_path = Path("files/text_2.txt")
    text_output = read_path.read_text()
    some_number = 1/0  # This will raise ZeroDivisionError
except FileNotFoundError:
    # Handle case when file doesn't exist
    text_output = "Default text"
    print("Error reading file, using default instead.")
except ZeroDivisionError:
    # Handle division by zero
    print("Number was divided by 0")
except:
    # Catch-all for any other exceptions
    ...

print("Retrieved text: ", text_output)

# === EXAMPLE 9: Iterating through directory contents ===
from pathlib import Path

path = Path("files")  # Create Path object for directory

files_string = list(path.iterdir())  # Convert iterator to list
files_iterable = path.iterdir()  # Get iterator of directory contents

# Iterate through each file in the directory
for f in files_iterable:
    file_text = f.read_text()  # Read each file's content
    print(file_text)