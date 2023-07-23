"""
Try to find out if a number you received from the user is the "Armstrong" number.

For example, if a number is 4 digits and it is the sum of the 4th power of each of its constituent digits (3rd power for 3 digit numbers)
If it is equal to that number, this number is called the "Armstrong" number.

For example : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

number = input("Enter a number:")
number_digits = len(number)
number = int(number)
step = 0
total = 0

temp_number = number

while(temp_number > 0):
    step = temp_number % 10
    total += step ** number_digits
    temp_number //= 10

if(total == number):
    print("This number is an Armstrong number.")
else:
    print("This number is not an Armstrong number.")
