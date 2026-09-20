# Python Booleans - Learning Notes
# A boolean value is either True or False.
# Booleans are used for decisions and conditions.

# Example 1: Boolean values used in arithmetic
# In Python, True behaves like 1 and False behaves like 0.
is_boiling = True  # Store the boolean value True.
steps_count = 5  # Store the integer value 5.

total_actions = steps_count + is_boiling  # Add 5 and True, which acts like 1.
print(f"Total actions: {total_actions}")  # Print the result of the arithmetic.

# Example 2: Using bool() to check truthiness
# 0 is False, and any non-zero number is True.
milk_present = 0  # Store 0 to represent no milk.
print(f"Is there milk? {bool(milk_present)}")  # Convert 0 to a boolean value.

# Example 3: Logical AND
# The 'and' operator returns True only when both values are True.
water_hot = True  # Water is hot.
tea_added = True  # Tea has been added.

can_serve_chai = water_hot and tea_added  # Both conditions must be True to serve tea.
print(f"Can serve chai? {can_serve_chai}")  # Print the result of the condition.

# Summary:
# - Booleans are True or False.
# - bool(0) is False.
# - bool(non-zero) is True.
# - A and B is True only if both are True.