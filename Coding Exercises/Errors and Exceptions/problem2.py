"""
Write a function that queries whether a number is even. This function returns this value with *return* if the number
is even. However, if the number is odd, the function *raise* throws *ValueError*. Next, define a list that contains
even and odd numbers, and scroll through the list and print only even numbers to the screen.

"""

def even(number):
    if number % 2 == 0:
        return number
    else:
        raise ValueError

list1 = [13, 56, 73, 83, 32, 16, 21]

for i in list1:
    try:
        print(even(i))
    except ValueError:
        pass

