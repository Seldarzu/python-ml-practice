def get_user_info():
    name= input("Enter your name: ")
    print()
    height=input("Enter your height: ")
    return name,height



def main():
    
    name,height=get_user_info()

    print(name,"= ",height)

main()