def main():
    elements =(True,3.2,7,"goat")

    (is_raining,weight,volume,animal)=elements

    print (is_raining)
    print (weight)
    print (volume)
    print (animal)


    fruits = ("apple","banana","orange","strawberry","pear")

    (fruit1,fruit2,fruit3,*more_fruits)=fruits

    print()
    print(fruit1)
    print(fruit2)
    print(fruit3)
    print(more_fruits)

    print(type(more_fruits))

    one_item="goat"
main()