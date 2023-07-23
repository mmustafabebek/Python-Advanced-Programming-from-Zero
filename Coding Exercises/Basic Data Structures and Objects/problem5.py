# Ask the user for two numbers and exchange their values with each other.

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

print("Values Before Changing\na: {}\nb: {}\n".format(a,b))

a,b = b,a

print("Values After Changed\na: {}\nb: {}\n".format(a,b))