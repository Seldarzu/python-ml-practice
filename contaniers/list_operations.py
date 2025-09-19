def main():
    # -----------------------------
    # Part 1: Adding and extending lists
    # -----------------------------
    animals = ["dog", "donkey", "duck"]

    # Insert "giraffe" at index 1
    animals.insert(1, "giraffe")
    print(animals)

    # Create another list of animals
    more_animals = ["elephant", "monkey"]

    # Extend animals list by adding elements from more_animals
    animals.extend(more_animals)
    print(animals)

    print("-----------------------------")

    # -----------------------------
    # Part 2: Removing items from lists
    # -----------------------------
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Remove the first 3 elements using slicing
    days[0:3] = []
    print(days)

    # Remove a specific item by value
    days.remove("Sat")
    print(days)

    # Remove and return the first element using pop
    item = days.pop(0)
    print(days)
    print(item)

    print("-----------------------------")

    # -----------------------------
    # Part 3: Deleting, clearing lists
    # -----------------------------
    # Pop element at index 0 again
    item = days.pop(0)
    print(days)
    print(item)

    # Delete element at index 1
    del days[1]
    print(days)

    # Clear the entire list (make it empty)
    days.clear()
    print(days)

    # Delete the whole list object
    del days
    # print(days)  # This would cause an error because days no longer exists


main()
