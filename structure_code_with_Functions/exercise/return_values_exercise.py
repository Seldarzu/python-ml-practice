"""
Write a funtion that asks the user to enter their weight in kilos
and their height in metres.than calculatues their BMI

(weight divided by height time height)

The function should return all three values.
"""

def bmi():
    height=float(input("Enter your height(metres): "))
    weight=float(input("Enter your weight(kilos): "))
    bmi=weight/(height*height)
    return height,weight,bmi

def main():
    height, weight, bmi_value = bmi()
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi_value:.2f}") 
main()