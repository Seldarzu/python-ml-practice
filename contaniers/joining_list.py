animals1 = ("dog", "cat", "mouse")
animals2 = ("lion", "tiger", "elephant")

fruits1 = ["apple", "orange"]
fruits2 = ["strawberry", "melon", "grape"]

value = 5
value += 3   # Same as value = value + 3
print()

# Tuples are immutable, so concatenation creates a new object
print(id(animals1))        # ID of the original tuple
animals1 += animals2       # Creates a new tuple and reassigns animals1
print(animals1)
print(id(animals1))        # ID is different because a new object was created
print()

# Lists are mutable, so += modifies the existing object
print(type(fruits1))       # Confirm it's a list
print(id(fruits1))         # ID of the original list
fruits1 += fruits2         # Extends the list in place
print(fruits1)
print(id(fruits1))         # ID is the same because the object was modified
print(type(fruits1))       # Still a list
print()

# Print the updated value
print(value)
