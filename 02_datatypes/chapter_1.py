# Python Variables - Learning Notes
# Variables store values so we can use them later in the program.

# Example 1: Assigning an integer value to a variable
sugar_amount = 2  # Store the integer 2 in the variable sugar_amount.
print(f"Initial sugar: {sugar_amount}")  # Print the value currently stored in sugar_amount.

# Example 2: Reassigning the variable with a new value
sugar_amount = 12  # Change the variable to hold the new value 12.
print(f"Updated sugar: {sugar_amount}")  # Print the updated value.

# Example 3: Checking object IDs
# Every value in Python may have a unique identity in memory.
print(f"ID of 2: {id(2)}")  # Print the memory identity of the integer 2.
print(f"ID of 12: {id(12)}")  # Print the memory identity of the integer 12.

# Summary:
# - Variables can hold values.
# - Their values can be changed later.
# - Python stores values in memory and gives each object an ID.
# - This helps us understand how data is stored.