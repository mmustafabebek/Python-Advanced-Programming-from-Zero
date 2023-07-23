"""
Take the two perpendicular sides (a, b) of a right triangle from the user and try to find the length of the hypotenuse.
Hypotenuse Formula: a^2 + b^2 = c^2
"""

a = int(input("Enter the first right side of the right triangle:"))
b = int(input("Enter the second right side of the right triangle:"))
c = (a ** 2 + b ** 2) ** 0.5

print("Hypotenuse Length: ",c)