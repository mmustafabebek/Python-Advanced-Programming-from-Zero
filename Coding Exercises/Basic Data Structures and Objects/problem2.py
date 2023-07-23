# Find the user's body mass index based on the height and weight values you get from the user.
# Body Mass Index: Weight / Height(m) Height(m)

height = float(input("Enter your height information:"))
weight = int(input("Enter your weight information:"))

bodymassindex = input("Your Body Mass Index: {}\n".format(weight / height ** 2))