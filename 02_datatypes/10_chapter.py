# Python Dictionaries - Zero to Hero Learning Notes
# A dictionary stores data as key-value pairs.
# It is useful when you want to store related information together.

# Example 1: Create a dictionary for a chai order
chai_order = dict(type="Masala Chai", size="Large", sugar=2)  # Create a dictionary with details.
print(f"Chai order: {chai_order}")  # Print the whole dictionary.

# Example 2: Add values to an empty dictionary
chai_recipe = {}  # Create an empty dictionary.
chai_recipe["base"] = "black tea"  # Add the key 'base' with value 'black tea'.
chai_recipe["liquid"] = "milk"  # Add the key 'liquid' with value 'milk'.

print(f"Recipe base: {chai_recipe['base']}")  # Read the value for the 'base' key.
print(f"Recipe: {chai_recipe}")  # Print the full recipe dictionary.

del chai_recipe["liquid"]  # Remove the 'liquid' key-value pair.
print(f"Recipe after removal: {chai_recipe}")  # Print the dictionary after deletion.

# Example 3: Check if a key exists
print(f"Is sugar in the order? {'sugar' in chai_order}")  # Check whether 'sugar' is a key.

# Example 4: Replace a dictionary with new values
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}  # Create a new chai order.

# print(f"Order details (keys): {chai_order.keys()}")  # Show all keys in the dictionary.
# print(f"Order details (values): {chai_order.values()}")  # Show all values in the dictionary.
# print(f"Order details (items): {chai_order.items()}")  # Show all key-value pairs.

# Example 5: Remove the last inserted item
last_item = chai_order.popitem()  # Remove and return the last key-value pair.
print(f"Removed last item: {last_item}")  # Print the removed pair.

# Example 6: Update a dictionary with more data
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}  # Create a dictionary of extra spices.
chai_recipe.update(extra_spices)  # Add the extra spice information to the recipe.
print(f"Updated chai recipe: {chai_recipe}")  # Print the updated recipe.

# Example 7: Get a value safely
customer_note = chai_order.get("size", "NO Note")  # Get the size, or use a default if missing.
print(f"customer_note is: {customer_note}")  # Print the result.

# Summary:
# - Dictionaries store data as key-value pairs.
# - Keys are unique, and values can be anything.
# - You can add, delete, update, and read data from a dictionary.
# - .get() is a safe way to read a key without raising an error.