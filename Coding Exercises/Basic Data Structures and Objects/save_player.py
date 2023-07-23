print("Player Registration Program")

name = input("Player Name:")
lastname = input("Player's Last Name:")
team = input("Player's Team:")

informations = [name,lastname,team]

print("\nSaving Information....\n")

print("Player Name: {}\nPlayer's Last Name: {}\nPlayer's Team: {}\n".format(informations[0],informations[1],informations[2]))


print("Information Saved.....")