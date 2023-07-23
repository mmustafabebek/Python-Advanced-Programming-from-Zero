# Get 3 numbers from the user and print the largest number on the screen.

a = float(input("First Number:"))
b = float(input("Third Number:"))
c = float(input("Second Number:"))

if (a > b and a > c):
    print("Biggest number is {}.".format(a))
elif (b > a and b > c):
    print("Biggest number is {}.".format(b))
elif (c > a and c > b):
    print("Biggest number is {}.".format(c))
