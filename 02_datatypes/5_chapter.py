# Python Float Numbers - Learning Notes
# Float values are numbers with decimal points.
# They are used for measurements, temperature, price, and many other real-world values.

import sys  # Import the sys module to access float information.
from fractions import Fraction  # Import Fraction for exact rational values.
from decimal import Decimal  # Import Decimal for precise decimal arithmetic.

# Example 1: Temperature values
ideal_temp = 95.5  # Store the ideal temperature as a float.
current_temp = 95.49  # Store the current temperature as a float.

print(f"Ideal temperature: {ideal_temp}")  # Print the ideal temperature.
print(f"Current temperature: {current_temp}")  # Print the current temperature.
print(f"Temperature difference: {ideal_temp - current_temp}")  # Subtract to find the difference.

# Example 2: Python float information
# Python stores float values in binary format, so some decimals may not be exact.
print(sys.float_info)  # Print information about floating-point limits.

# Example 3: Fraction for exact values
# Fraction keeps numbers exact, without floating-point rounding issues.
exact_fraction = Fraction(1, 3)  # Create an exact fraction of one third.
print(f"Exact fraction value: {exact_fraction}")  # Print the exact fraction.

# Example 4: Decimal for precise decimal arithmetic
# Decimal is useful when exact decimal calculation matters, such as money.
exact_decimal = Decimal("0.1") + Decimal("0.2")  # Add two decimals exactly.
print(f"Exact decimal result: {exact_decimal}")  # Print the precise decimal answer.

# Summary:
# - float is good for normal decimal calculations.
# - float may have minor precision issues.
# - Fraction gives exact mathematical results.
# - Decimal is best for exact decimal values like currency.