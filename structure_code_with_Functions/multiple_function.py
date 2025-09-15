PASSWORD="hello"

def greeting():
    print("Welcome ! No unauthorised users.")

def check_password():
    password=input("Enter your password: ")

    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied.")
"""
In Python, defining a main() function is not mandatory, since the interpreter executes code from top to bottom. However, when a program grows and contains multiple functions or modules, it is considered a good practice to define a main() function.

This approach provides several benefits:

✅ It clearly indicates the entry point of the program.

✅ It makes the codebase more organized and readable.

✅ It supports the if __name__ == "__main__": idiom, which prevents certain parts of the code from running when the file is imported as a module.

✅ It is a standard convention in professional projects, making your code more maintainable and familiar to other developers.
"""
def main():
    greeting()
    check_password()


main()