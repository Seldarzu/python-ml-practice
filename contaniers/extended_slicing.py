numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven"]

# Slice from index 3 to 7 (exclusive), stepping by 2
print(numbers[3:7:2])

# Replace elements in the slice [3:7:2] with new values
numbers[3:7:2] = ["hello", "hi"]
print(numbers)

# Copy the entire list using slicing
print(numbers[::])

# String slicing: take every 2nd character
greeting = "Hello there"
print(greeting[::2])

# String slicing: start from index 3, take every 3rd character
print("What are you?"[3::3])
