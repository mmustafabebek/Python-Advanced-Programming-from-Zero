# Multiply the 3 numbers you receive from the user and print them on the screen. Try to print to the screen with the *format* method.

a = int(input("First Number:"))
b = int(input("Second Number:"))
c = int(input("Third Number:"))

multiplication = a * b * c

print("First Number: {}\nSecond Number: {}\nThird Number: {}\nMultiplication of Numbers: {}".format(a,b,c,multiplication))