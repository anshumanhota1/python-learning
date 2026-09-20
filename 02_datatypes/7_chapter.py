# Python Tuples - Learning Notes
# A tuple is an ordered collection of values.
# Tuples are immutable, which means their values cannot be changed after creation.

# Example 1: Creating a tuple
masala_spices = ("cardamom", "cloves", "cinnamon")  # Store a fixed list of spice names.
print(f"Masala spices: {masala_spices}")  # Print the tuple.

# Example 2: Tuple unpacking
# This assigns each element of the tuple to a separate variable.
(spice1, spice2, spice3) = masala_spices  # Assign each item to a different variable.
print(f"Spice 1: {spice1}")  # Print the first spice.
print(f"Spice 2: {spice2}")  # Print the second spice.
print(f"Spice 3: {spice3}")  # Print the third spice.

# Example 3: Swapping values using tuple assignment
# This is a neat Python trick to swap two values without a temporary variable.
ginger_ratio, cardamom_ratio = 2, 1  # Store two values in one line.
print(f"Before swap: ginger = {ginger_ratio}, cardamom = {cardamom_ratio}")  # Show the original values.

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio  # Swap both values in one step.
print(f"After swap: ginger = {ginger_ratio}, cardamom = {cardamom_ratio}")  # Print the swapped values.

# Example 4: Membership testing
# The 'in' operator checks whether an item exists in the tuple.
print(f"Is 'cinnamon' in masala_spices? {'cinnamon' in masala_spices}")  # Check if cinnamon exists.

# Summary:
# - Tuples store related values together.
# - They are useful when the values should not change.
# - Tuple unpacking makes code easier to read.
# - The 'in' keyword checks membership quickly.