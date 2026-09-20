# Python Lists - Learning Notes
# A list is an ordered, changeable collection of items.

# Example 1: Add and remove items
ingredients = ["water", "milk", "black tea"]  # Create a list of ingredients.
ingredients.append("sugar")  # Add 'sugar' to the end of the list.
print(f"Ingredients are: {ingredients}")  # Print the list after adding sugar.
ingredients.remove("water")  # Remove 'water' from the list.
print(f"Ingredients are: {ingredients}")  # Print the list after removal.

# Example 2: Extend and insert items
spice_options = ["ginger", "cardamom"]  # Create a list of spice choices.
chai_ingredients = ["water", "milk"]  # Create a list of base chai ingredients.

chai_ingredients.extend(spice_options)  # Add all spice options to the chai list.
print(f"chai: {chai_ingredients}")  # Print the new list.
chai_ingredients.insert(2, "black tea")  # Insert 'black tea' at index 2.
print(f"chai: {chai_ingredients}")  # Print the list after insertion.

# Example 3: Pop, reverse, and sort
last_added = chai_ingredients.pop()  # Remove and return the last item from the list.
print(f"{last_added}")  # Print the item removed from the end.
print(f"chai: {chai_ingredients}")  # Print the remaining list.
chai_ingredients.reverse()  # Reverse the list order.
print(f"chai: {chai_ingredients}")  # Print the reversed list.
chai_ingredients.sort()  # Sort the list in ascending order.
print(f"chai: {chai_ingredients}")  # Print the sorted list.

# Example 4: Minimum and maximum values
sugar_levels = [1, 2, 3, 4, 5]  # Create a list of sugar intensity levels.
print(f"Maximum sugar level: {max(sugar_levels)}")  # Print the largest value in the list.
print(f"Minimum sugar level: {min(sugar_levels)}")  # Print the smallest value in the list.

# Example 5: Concatenation and repetition
base_liquid = ["water", "milk"]  # Create a list of base liquids.
extra_flavor = ["ginger"]  # Create a list of extra flavor ingredients.

full_liquid_mix = base_liquid + extra_flavor  # Join both lists together.
print(f"Liquid mix: {full_liquid_mix}")  # Print the combined list.

strong_brew = ["black tea", "water"] * 3  # Repeat the list three times.
print(f"String brew: {strong_brew}")  # Print the repeated list.

# Example 6: Bytearray operations
raw_spice_data = bytearray(b"CINNAMON")  # Create a bytearray of bytes.
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")  # Replace a byte pattern.
print(f"Bytes: {raw_spice_data}")  # Print the modified bytearray.

# Summary:
# - Lists are ordered and mutable.
# - append() adds an item at the end.
# - remove() deletes an item.
# - extend() adds multiple items.
# - insert() adds an item at a chosen position.
# - pop() removes and returns the last item.
# - reverse() changes the order.
# - sort() arranges values in order.
# - + combines lists and * repeats them.