def describe_person(name,*attributes):
    print(name)

    for attribute in attributes:
        print(attribute)




def main():
    
    describe_person("Cem Yılmaz", "witty", "observational", "charismatic")
    print()
    describe_person("Ata Demirer", "funny", "musical", "imitator")
    print()
    describe_person("Hasan Can Kaya", "energetic", "interactive")
    print()

    
    describe_person("Dave Chappelle", "provocative", "insightful", "funny")
    print()
    describe_person("Kevin Hart", "energetic", "fast-talking")
    print()
    describe_person("Ricky Gervais", "sarcastic", "controversial", "dark humor")
    print()
    describe_person("Ali Wong", "sharp", "fearless", "relatable")
    print()

main()