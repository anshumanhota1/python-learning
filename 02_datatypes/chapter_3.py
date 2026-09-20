# Integer arithmetic in Python
# These are basic arithmetic operations using integers.

# 1. Addition
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea base: {total_grams} g")

# 2. Subtraction
remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining tea after subtraction: {remaining_tea} g")

# 3. Division
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving} litres")

# 4. Floor division
# It gives the whole-number quotient without the decimal part.
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot: {bags_per_pot}")

# 5. Modulus
# It gives the remainder after division.
total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# 6. Exponentiation
base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength: {powerful_flavour}")
# 2 * 2 * 2 = 8

# 7. Numeric separators for readability
# Python allows underscores in large numbers.
total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")
