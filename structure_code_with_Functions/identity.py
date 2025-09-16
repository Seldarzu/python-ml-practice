def greet(name):
    print(id(name))
    print("Hello "+name)

"""
pass
 In Python, if you define a function without providing a body, the interpreter will raise an error.
 To avoid this, you can use the pass statement as a placeholder,
 which tells Python to do nothing and allows the function to be syntactically valid.
"""
def main():
   
    name="Arzu"

    print(id(name))
    greet(name)


main()