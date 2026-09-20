# Shopping List Exercise - beginner friendly
# This exercise teaches common list operations in Python.

# 1. Create a grocery list named my_cart with the items: apples, bananas, and milk
my_cart = ["apples", "bananas", "milk"]  # Create a list of grocery items.
print(f"Initial grocery list: {my_cart}")  # Print the list.

# 2. Add "bread" to the end of the list.
my_cart.append("bread")  # Add bread at the end of the list.
print(f"After adding bread: {my_cart}")  # Show the updated list.

# 3. Insert "ketchup" at the beginning of the list.
my_cart.insert(0, "ketchup")  # Add ketchup at index 0, which is the beginning.
print(f"After inserting ketchup at the beginning: {my_cart}")  # Show the updated list.

# 4. Remove "bananas" from the list.
my_cart.remove("bananas")  # Remove bananas from the list.
print(f"After removing bananas: {my_cart}")  # Show the list after removal.

# 5. Remove the last item from the list and store it in a variable named removed_item.
removed_item = my_cart.pop()  # Remove and return the last item.
print(f"Removed item: {removed_item}")  # Print the removed item.

# 6. Extend the grocery list by adding "rice" and "butter".
my_cart.extend(["rice", "butter"])  # Add both items to the end of the list.
print(f"After extending with rice and butter: {my_cart}")  # Show the updated list.

# 7. Sort the grocery list in alphabetical order.
my_cart.sort()  # Arrange the words in alphabetical order.
print(f"After sorting: {my_cart}")  # Show the sorted list.

# 8. Reverse the order of the grocery list.
my_cart.reverse()  # Reverse the list order.
print(f"After reversing: {my_cart}")  # Show the reversed list.

# 9. Concatenate the grocery list with another list containing "juice" and "jam".
other_items = ["juice", "jam"]  # Create a second list.
combined_list = my_cart + other_items  # Join both lists together.
print(f"After concatenation: {combined_list}")  # Print the combined result.

# 10. Duplicate the grocery list twice.
repeated_list = my_cart * 2  # Repeat the list two times.
print(f"After duplicating twice: {repeated_list}")  # Print the repeated list.

# 11. Define a string with the value "tomato cucumber spinach" and convert it into a list.
shopping_text = "tomato cucumber spinach"  # Create a string with words separated by spaces.
shopping_list_from_text = shopping_text.split()  # Split the string into a list of words.
print(f"Converted list from string: {shopping_list_from_text}")  # Print the new list.

# Summary:
# - append() adds to the end
# - insert() adds at a specific position
# - remove() deletes a value
# - pop() removes the last item
# - extend() adds multiple items
# - sort() arranges in order
# - reverse() flips the order
# - + combines lists
# - * repeats a list
# - split() converts a string to a list
