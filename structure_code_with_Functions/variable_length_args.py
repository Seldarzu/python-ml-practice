def add_description(**description):
    
    for prop in description:
        print(prop,": ",description[prop])

    print()



def main():
    add_description(height=180,weight="90",eyes="green")
    add_description(shirt=True,beard="yellow",sex="women")
    add_description(age=34,purse=False,hair="ginger")

    
    


main()