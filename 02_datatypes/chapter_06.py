# Python Strings - Learning Notes
# Strings are sequences of characters used to store text.

# Example 1: Creating and printing a string
chai_type = "Ginger chai"  # Store the type of chai as a string.
customer_name = "Priya"  # Store a customer name as a string.

print(f"Order for {customer_name}: {chai_type}, please!")  # Print a formatted message using both strings.

# Example 2: String slicing
# Slicing lets you take parts of a string.
chai_description = "Aromatic and Bold"  # Store a description as a string.
print(f"First 8 characters: {chai_description[:8]}")  # Print the first 8 characters.
print(f"Characters from index 12 onward: {chai_description[12:]}")  # Print from index 12 to the end.
print(f"Reversed string: {chai_description[::-1]}")  # Reverse the string using slicing.

# Example 3: Encoding and decoding strings
# Encoding converts text into bytes.
# Decoding converts bytes back into text.
label_text = "Chai Spécial"  # Store a string with a special character.
encoded_label = label_text.encode("utf-8")  # Convert the string to bytes using UTF-8.
print(f"Original label: {label_text}")  # Print the original text.
print(f"Encoded label: {encoded_label}")  # Print the encoded bytes.

decoded_label = encoded_label.decode("utf-8")  # Convert the bytes back to a string.
print(f"Decoded label: {decoded_label}")  # Print the decoded text.

# Summary:
# - Strings hold text data.
# - Slicing helps access specific parts of text.
# - encode() converts text to bytes.
# - decode() converts bytes back to text.