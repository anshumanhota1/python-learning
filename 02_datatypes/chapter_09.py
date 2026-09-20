# Python Sets - Zero to Hero Learning Notes
# A set is a collection of unique items.
# It does not keep duplicate values, and it is not ordered like a list.

# Example 1: Create two sets of spices
essential_spices = {"cardamom", "ginger", "cinnamon"}  # A set of must-have spices.
optional_spices = {"cloves", "ginger", "black pepper"}  # A set of optional spices.

print(f"Essential spices: {essential_spices}")  # Print the first set.
print(f"Optional spices: {optional_spices}")  # Print the second set.

# Example 2: Union
# Union combines both sets and removes duplicates.
all_spices = essential_spices | optional_spices  # Join both sets together.
print(f"All spices: {all_spices}")  # Show all unique spices from both sets.

# Example 3: Intersection
# Intersection finds the items that are in both sets.
common_spices = essential_spices & optional_spices  # Keep only the shared values.
print(f"Common spices: {common_spices}")  # Print the spices that appear in both sets.

# Example 4: Difference
# Difference shows items in the first set that are not in the second set.
only_in_essential = essential_spices - optional_spices  # Keep only the unique items from essential_spices.
print(f"Only in essential spices: {only_in_essential}")  # Print the items that are special to the first set.

# Example 5: Membership test
# 'in' checks whether a value exists in the set.
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")  # Check if cloves is present.

# Summary:
# - Sets hold unique values only.
# - | is union: combine two sets.
# - & is intersection: keep common values.
# - - is difference: keep items only in one set.
# - 'in' checks whether an item is present.
# - Sets are great for uniqueness and fast membership checks.