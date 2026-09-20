# Python Sets - Learning Notes
# A set is an unordered collection of unique items.
# It does not keep duplicate values.

# Example 1: Create an empty set
spice_mix = set()  # Create an empty set that can store unique values.
print(f"Initial spice mix: {spice_mix}")  # Print the empty set.
print(f"Memory id of spice_mix: {id(spice_mix)}")  # Show the memory identity of the set object.

# Example 2: Add items to the set
spice_mix.add("Ginger")  # Add the value 'Ginger' to the set.
spice_mix.add("Cardamom")  # Add the value 'Cardamom' to the set.
print(f"Spice mix after adding items: {spice_mix}")  # Print the updated set contents.
print(f"Memory id after adding items: {id(spice_mix)}")  # Show that it is still the same set object.

# Summary:
# - Sets store unique values only.
# - Sets are unordered, so order is not guaranteed.
# - The id stays the same because we are modifying the same set object.
# - Use add() to insert new elements into a set.
