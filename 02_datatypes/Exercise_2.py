# Should You Go for a Walk? - beginner friendly
# This exercise teaches boolean logic using real-life conditions.

is_sunny = True  # It is sunny today.
have_umbrella = False  # You do not have an umbrella.

# 1. Is it not sunny today?
not_sunny = not is_sunny  # The not operator reverses True into False.
print(f"Is it not sunny today? {not_sunny}")  # Print the result.

# 2. Do you not have an umbrella?
no_umbrella = not have_umbrella  # Reverse False to True.
print(f"Do you not have an umbrella? {no_umbrella}")  # Print the result.

# 3. Should you go for a walk if it’s sunny and you don’t need an umbrella?
should_walk_if_sunny_and_no_umbrella = is_sunny and not have_umbrella  # Both conditions must be True.
print(f"Should you go for a walk if it’s sunny and you don’t need an umbrella? {should_walk_if_sunny_and_no_umbrella}")  # Print the result.

# 4. Should you go for a walk if it’s sunny or if you have an umbrella?
should_walk_if_sunny_or_has_umbrella = is_sunny or have_umbrella  # Either condition can be True.
print(f"Should you go for a walk if it’s sunny or if you have an umbrella? {should_walk_if_sunny_or_has_umbrella}")  # Print the result.

# Summary:
# - not flips a boolean value
# - and means both must be True
# - or means at least one must be True