# dict_examples.py

def main():
    print("=== Basic Dictionary ===")
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
        True: 7
    }

    print(fruits["apple"])
    print(fruits["orange"])
    print(fruits["banana"])
    print(fruits[True])

    print("\n=== Updating Dictionary ===")
    months = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
    }

    months["Apr"] = "April"  #add a new key-value pair
    months.update({"May": "May", "Jun": "June"})  # add multiple pairs with update
    print(months)

    print("\n=== Iterating over keys ===")
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    for fruit in fruits.keys():
        print(fruit + ": " + fruits[fruit])

    print("apple" in fruits)

    print("\n=== Iterating with items() ===")
    for fruit, color in fruits.items():
        print(fruit + ", " + color)

    print("\n=== Iterating over values ===")
    for color in fruits.values():
        print(color)

    print("\n=== Keys, Values, Items Objects ===")
    keys = fruits.keys()
    values = fruits.values()
    items = fruits.items()

    print(keys)
    print(values)
    print(items)

    keys_list = list(keys)
    print(keys_list)

    print("\n=== After Adding New Key ===")
    fruits["raspberry"] = "red"
    print(fruits)

    print(keys)       # the keys view updates automatically
    print(keys_list)  # the list remains unchanged


if __name__ == "__main__":
    main()
