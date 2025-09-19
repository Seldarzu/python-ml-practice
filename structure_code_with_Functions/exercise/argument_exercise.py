"""
one or more positinal arguments
zero or more variable arguments
zero or more variable keyword arguments

Make the function print out all arguments it recevies.
"""

def test(name,*args,**kwargs):
    print(name)
    print()

    for arg in args:
        print(arg)

    for kywrd in kwargs:
        print(kywrd,"=",kwargs[kywrd]) 
print()


def main():
    test("Bob",1,2,3,color="red",value =8)
    test("Bob",1,2,"hello",color="red",value =8)
main()