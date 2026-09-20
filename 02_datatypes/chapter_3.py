# Python Integer Arithmetic - Learning Notes
# Integers are whole numbers. Python supports many arithmetic operations on them.

# Example 1: Addition
black_tea_grams = 14  # Store the first integer value.
ginger_grams = 3  # Store the second integer value.

total_grams = black_tea_grams + ginger_grams  # Add both numbers together.
print(f"Total grams of tea base: {total_grams} g")  # Print the sum.

# Example 2: Subtraction
remaining_tea = black_tea_grams - ginger_grams  # Subtract ginger from black tea.
print(f"Remaining tea after subtraction: {remaining_tea} g")  # Print the result.

# Example 3: Division
# / gives a floating-point result.
milk_litres = 7  # Store the total milk in litres.
servings = 4  # Number of servings.
milk_per_serving = milk_litres / servings  # Divide milk by number of servings.
print(f"Milk per serving: {milk_per_serving} litres")  # Print the float result.

# Example 4: Floor division
# // gives only the whole-number part.
total_tea_bags = 7  # Total tea bags available.
pots = 4  # Number of pots.
bags_per_pot = total_tea_bags // pots  # Divide and keep only the whole number.
print(f"Tea bags per pot: {bags_per_pot}")  # Print the integer result.

# Example 5: Modulus
# % gives the remainder after division.
total_cadamom_pods = 10  # Total number of cardamom pods.
pods_per_cup = 3  # Pods that fit in one cup.
leftover_pods = total_cadamom_pods % pods_per_cup  # Check the remainder after division.
print(f"Leftover cardamom pods: {leftover_pods}")  # Print the remainder.

# Example 6: Exponentiation
# ** means power.
base_flavor_strength = 2  # Base value.
scale_factor = 3  # Power to apply.
powerful_flavour = base_flavor_strength ** scale_factor  # Raise base to the given power.
print(f"Scaled flavour strength: {powerful_flavour}")  # Print the result.
# 2 * 2 * 2 = 8

# Example 7: Numeric separators
# Underscores make large numbers easier to read.
total_tea_leaves_harvested = 1_000_000_000  # Large number written in a readable form.
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")  # Print the value.

# Summary:
# + adds numbers
# - subtracts numbers
# / divides and returns float
# // divides and returns integer part
# % gives the remainder
# ** raises a number to a power
