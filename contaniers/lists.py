def main():
    # Create a list of fruits
    fruits = ["apple", "orange", "banana"]

    # Print the length of the list
    print(len(fruits))

    # Print the element at index 2 ("banana")
    print(fruits[2])

    # Print a slice from index 0 up to (but not including) 2
    print(fruits[0:2])

    # Create an empty tuple and an empty list
    test1 = tuple()
    test2 = list()

    # Create a tuple of animals
    animals = ("fox", "rabbit")
    print(animals)

    # Convert the tuple into a list
    animals = list(animals)
    print(animals)

    # Iterate through the list and print each animal
    for animal in animals:
        print(animal)

main()
