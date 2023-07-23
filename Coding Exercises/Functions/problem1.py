"""
Print perfect numbers from 1 to 1000 on the screen. For this, write a function that returns whether a number is perfect.

A number is a perfect number if the sum of its divisors is equal to itself. For example, 6 is a perfect number.
(1 + 2 + 3 = 6).
"""

def perfect(number):
    total = 0
    for i in range(1,number):
        if(number % i == 0):
            total += i
        else:
            continue
    if(total == number):
        print(number)

for x in range(1,1001):
    perfect(x)
