"""
Print all the cubic numbers up to and including 729.
Print all the square numbers up to and including 729.

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?

"""
def main():
    cubic_set ={x**3 for x in range(1,10)}
    print(max(cubic_set))

    square_set ={x*x for x in range(1,28)}
    print(max(square_set))

     # 3. Hem küp hem kare olan sayılar (intersection)
    both = cubic_set.intersection(square_set)
    print("Both cubic and square:", both)

    # 4. Küp olup kare olmayan sayılar (difference)
    only_cubic = cubic_set - square_set
    print("Cubic but not square:", only_cubic)

main()