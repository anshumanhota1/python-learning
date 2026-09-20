# Swapping temperature values back to the correct order - beginner friendly
# Sometimes values are entered in the wrong order, so we swap them.

min_temp = 40  # Current minimum value is stored here.
max_temp = 25  # Current maximum value is stored here.

# Tuple unpacking lets us swap both values in one line.
min_temp, max_temp = max_temp, min_temp  # Swap the values.

print(f"Correct minimum temperature: {min_temp}")  # Show the corrected minimum value.
print(f"Correct maximum temperature: {max_temp}")  # Show the corrected maximum value.

# Summary:
# - We use tuple unpacking to swap values quickly.
# - This is a common beginner-friendly Python trick.