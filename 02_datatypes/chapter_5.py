# Floating point numbers in Python
# Float values are used for numbers with decimal points.

import sys
from fractions import Fraction
from decimal import Decimal

# Example: temperature values
ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Temperature difference: {ideal_temp - current_temp}")

# Python float precision is limited
# This means some decimal values may not be stored exactly.
print(sys.float_info)

# Fraction gives exact rational values
# Useful when you need precision without rounding issues.
exact_fraction = Fraction(1, 3)
print(f"Exact fraction: {exact_fraction}")

# Decimal gives precise decimal arithmetic
# It is useful for money or scientific calculations.
exact_decimal = Decimal("0.1") + Decimal("0.2")
print(f"Exact decimal result: {exact_decimal}")

# Notes:
# - float is good for general numerical work
# - Decimal is better for precision-sensitive values
# - Fraction is useful for exact mathematical values