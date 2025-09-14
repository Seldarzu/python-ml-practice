#The Fridge

"""
Get the use to enter a temperature in celsius.

<0  :Print "Fridge too cold"
0-4 :Print "Fridge OK" 
4-6 :Print "Fridge too warm"
>6  :Print "Fridge broken"


"""

celsius=float(input("Enter the fridge temperature:"))
""""
if celsius < 0:
    print("Fridge too cold")
elif 0<=celsius<4:
    print("Fridge OK")
elif 4<=celsius<6:
    print("Fridge too warm")
else:
    print("Fridge broken")
   """     
status = "Fridge is broken"
if celsius <0:
    status="Fridge too cold"
elif celsius <=4:
    status ="Fridge OK"
elif celsius <=6:
    status="Fridge too warm"
print(status)