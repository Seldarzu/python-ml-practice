def main(): 
    numbers=[[1,2,3],[4,5,6],[7,8],[9,10,11,12]]

    sublist=numbers[1]

    print(sublist)

    print(sublist[2])

    print(numbers[2][1])


    for x in numbers:
        for y in x:
            print(y,end="")
        print()

    for i in range (0,len(numbers)):
        for j in range (0,len(numbers[i])):
            print(numbers[i][j],end=",")
        print()
main()