"""
Try to find out if a number you get from the user is perfect.

A number is called a "perfect number" if the sum of its divisors is equal to itself.
For example, 6 is a perfect number. (1 + 2 + 3 = 6)
"""

number = int(input("Enter a number:"))
dividing = 0

for i in range(1,number):
    if(number % i == 0):
        dividing += i
    else:
        continue

if(dividing == number):
    print("This number is a perfect number.")
else:
    print("This number is not a perfect number.")

