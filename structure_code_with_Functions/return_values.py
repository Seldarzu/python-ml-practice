def simple_greeting():
    return "Hi there!"

def customer_greeting(name):
    print("Hello "+name)

def friendly_greeting(name):
    return "What's up "+name


def main():

    name=input("What is your name: ")

    simple=simple_greeting()
    print(simple)

    friendly=friendly_greeting(name)
    print(friendly)

    customer_greeting(name)

main()    

