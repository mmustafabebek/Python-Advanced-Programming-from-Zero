"""
Calculate the body mass index according to the height and weight values obtained from the user and print the following
texts on the screen according to these rules.

 Body Mass Index: Weight / Height(m) * Height(m)

  If BMI is below 18.5 -------> Poor

  If BMI is between 18.5 and 25 ------> Normal

  If BMI is between 25 and 30 --------> Overweight

  If BMI is over 30 -------------> Obese
"""

print("""**************************************************
Body Mass Index Calculator
**************************************************""")

height = float(input("Your height:"))
weight = float(input("Your weight:"))

body_mass_index = weight / (height * height)

if (body_mass_index < 18.5):
    print("Weak")
elif (18.5 <= body_mass_index and body_mass_index < 25):
    print("Normal")
elif (25 <= body_mass_index and body_mass_index < 30):
    print("Overweight")
elif (body_mass_index > 30):
    print("Obese")
