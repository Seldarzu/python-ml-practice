"""
Ask the user:
1.Are you a student?
2.Do you have pets?
3.Do you smoke?

The program automatically decides whether a property you've applied to rent is avaliable to you.

It should print an appropriate response,like"Property available" or "Property unavaliable".

The program applies these creteria:

If you are a student,You can only rent the property if you do not have pets and do not smoke 
If you are not a student,you can rent the property if you smoke or have pets,but not if you both 
smoke and also have pets.
"""
student = input("Are you a student? (y/n): ").lower() == "y"
have_pets =input("Do you have pets?(y/n): ").lower() == "y"
smoke =input("Do you smoke?(y/n): ").lower() == "y"



if student == True:
    if not have_pets and not smoke:
        print("Property available")
    else:
        print("Property unavailable")    
else:
    if have_pets ^ smoke:
         print("Property available")
    else:
        print("Property unavailable") 

"""
if student and not have_pets and not smoke:
    print("Property available")
elif not student and (have_pets ^ smoke):
    print("Property available")
else:
    print("Property unavailable")

"""