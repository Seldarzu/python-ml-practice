"""
Write a function that calculates the factorial of a number.

the factorial of a number is defined like this:

n!=n*(n-1) (n-2)*....*3*2*1

the factorial of zero ,0!,is defined as 1.

Calculate the factorial of 7 

Hint:
Use a loop 
Create a variable before the loop,and have the 
loop repetedly alter the number that the variable
refers to.
"""
def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def main():
    number = int(input("Enter number for factorial calculation: ")) 
    fac = factorial(number)
    print(f"The factorial of {number} is {fac}")

main()
