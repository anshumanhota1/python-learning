# Python Libraries and namedtuple - Zero to Hero Learning Notes
# This example shows how Python libraries can help with real-world tasks.

import arrow  # Import the arrow library for date and time handling.

brewing_time = arrow.utcnow()  # Get the current UTC time.
print(f"Current UTC time: {brewing_time}")  # Print the UTC time.

brewing_time.to("Europe/Rome")  # Convert the time to the Rome timezone.
print(f"Rome time: {brewing_time}")  # Print the converted time.

from collections import namedtuple  # Import namedtuple to create a record with names.
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])  # Create a named tuple with fields.

# We can now create a value using the named fields.
my_chai = chaiProfile("sweet", "strong")
print(f"My chai profile: {my_chai}")  # Print the named tuple.

# Summary:
# - Libraries add extra features to Python.
# - namedtuple lets you create small structured records.
# - This makes code easier to read and manage.