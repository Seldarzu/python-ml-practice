# sets_examples.py

def main():
    print("==== SET CREATION & DUPLICATES ====")
    numbers = {1, 2, 3, 1}
    print(numbers)

    numbers_list = [2, 3, 3, 2, 5, 6]
    print(set(numbers_list))

    for number in numbers:
        print(number)

    print(3 in numbers)
    print(5 in numbers)

    print("\n==== ADD & UPDATE ====")
    numbers1 = {1, 2, 3}
    print(numbers1)

    numbers1.add(7)
    numbers1.add(9)
    print(numbers1)

    numbers2 = {10, 20, 30}
    numbers1.update(numbers2)
    print(numbers1)

    numbers1.update(["cat", "dog"])
    print(numbers1)

    print("\n==== REMOVE & DISCARD ====")
    numbers = {x for x in range(15)}
    print(numbers)

    numbers.remove(6)
    print(numbers)

    # numbers.remove(20)  # hata verir
    numbers.discard(20)  # hata vermez
    print(numbers)

    print("Iterating over set:")
    for x in numbers:
        print(x)

    print("\n==== SET OPERATIONS ====")
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 1}

    print(numbers1.union(numbers2))
    print(numbers1.intersection(numbers2))

    print("Difference")
    print(numbers1.difference(numbers2))
    print(numbers1 - numbers2)
    print(numbers2.difference(numbers1))

    print(numbers2.symmetric_difference(numbers1))

    print("\n==== DIFFERENCE UPDATE & SUPERSET ====")
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 1}

    numbers1.difference_update(numbers2)
    print(numbers1)

    print(numbers1.issuperset(numbers2))
    print({1, 2, 3}.issuperset({1, 2}))


if __name__ == "__main__":
    main()
