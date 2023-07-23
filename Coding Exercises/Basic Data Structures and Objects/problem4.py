# Get the name, surname and number information from the user and print them on the screen one after the other.

name = input("Enter your name:")
lastname = input("Enter your last name:")
number = input("Enter your number:")

informations = [name,lastname,number]

print("\nYour name: {}\nYour last name: {}\nYour number: {}\n".format(informations[0],informations[1],informations[2]))