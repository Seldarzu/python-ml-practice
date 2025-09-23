
# --- Deleting items from a dictionary ---
fruits = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

# Delete the key "apple" from the dictionary
del fruits["apple"]

print(fruits)

# Remove "banana" and return its value
color = fruits.pop("banana")
print(color)

print(fruits)


# --- Retrieving values from a dictionary ---
fruits = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

# Try to get a value for a missing key ("mango") -> returns None
color = fruits.get("mango")
print(color)
print(type(color))

# Get a missing key with a default value
color = fruits.get("mango", "red")
print(color)

# Get an existing key with a default (default ignored since key exists)
color = fruits.get("banana", "red")
print(color)


# --- Using defaultdict for safe dictionary lookups ---
from collections import defaultdict

# Create a defaultdict with default type int
people = defaultdict(int)

# Update dictionary with some values
people.update({"Bob": 45, "Sarah": 30})

print(people)

# Access existing key
print(people["Bob"])

# Access missing key ("Vicky") -> returns 0 because default=int
print(people["Vicky"])


# --- Copying and iterating over dictionaries ---
fruits1 = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

# Copy fruits1 to fruits2
fruits2 = fruits1.copy()

# Remove "apple" from fruits1
fruits1.pop("apple")

print(fruits1)
print(fruits2)

# Create a new dictionary from fruits2 keys
fruits3 = {x for x in fruits2}
print(fruits3)
