# Boolean data type in Python
# Booleans are either True or False.

# 1. Boolean values can be used with arithmetic in Python
is_boiling = True
steps_count = 5

# Python converts True to 1 and False to 0 in arithmetic
# This is called boolean-to-integer conversion.
total_actions = steps_count + is_boiling
print(f"Total actions: {total_actions}")

# 2. Using bool() to check truthiness
# 0 is considered False, and any non-zero value is considered True.
milk_present = 0  # no milk
print(f"Is there milk? {bool(milk_present)}")

# 3. Logical AND
water_hot = True
tea_added = True

can_serve_chai = water_hot and tea_added
print(f"Can serve chai? {can_serve_chai}")

# Note:
# - True and True -> True
# - True and False -> False
# - False and anything -> False