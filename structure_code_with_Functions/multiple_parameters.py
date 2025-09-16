"""
volume=width*height*length
"""


def volume_calculator(width,height,length):
    return width*height*length



def main():
    width=int(input("Width: "))
    height=int(input("Height: "))
    length=int(input("Length: "))


    volume=volume_calculator(width,height,length)
    print("Volume :",volume)


main()