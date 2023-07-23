"""
Write a function that takes 2 numbers from the user and returns the greatest common divisor (EBOB) of these numbers.
"""

def find_ebob(number1,number2):
    i = 1
    ebob = 1
    while(i <= number1 and i <= number2):
        if(not(number1 % i) and not(number2 % i)):
            ebob = i
        i += 1
    return ebob

number1 = int(input("Number1 :"))
number2 = int(input("Number2 :"))

print("EBOB :",find_ebob(number1,number2))
