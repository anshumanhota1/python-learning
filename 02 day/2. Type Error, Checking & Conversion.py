# Type Checking
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion 
print(int("123") + int("456"))

#Type Error
# print("Number of letters in your name: " + len (input("Enter your name ")))
name_of_the_user = input("Enter your name ")
length_of_name = len(name_of_the_user)
print(type("Number of letters in your name: "))
print(type(length_of_name))
print("Number of letters in your name: " + str(length_of_name))