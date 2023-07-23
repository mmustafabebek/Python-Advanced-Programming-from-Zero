"""
Take a 2-digit number from the user and write a function that finds the pronunciation of that number.

Example: 97 ---------> Ninety Seven
"""

ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
them = ["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
def pronunciation(number):
    first = number % 10
    second = number // 10

    return them[second] + " " + ones[first]

number = int(input("Enter a two digit number:"))

print(pronunciation(number))
