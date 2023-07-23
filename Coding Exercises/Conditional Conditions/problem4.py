"""
Now let's do the geometric figure calculation. First, ask the user whether they want to find the type of triangle or rectangle.

If the user answers "Rectangle", ask for 4 sides and try to find out if this rectangle is a square, rectangle, or an ordinary rectangle.

If the user answers "Triangle", ask for 3 sides and try to find out if this triangle is isosceles, equilateral or an ordinary triangle.
If the given sides do not indicate a triangle, write "Does not indicate a triangle" on the screen.
"""

number = input("Select the polygon whose type you want to find:\n1.Triangle\n2.Quadrilateral\n")

if(number == "1"):
    a = float(input("Enter the first side:"))
    b = float(input("Enter the second side:"))
    c = float(input("Enter the third side:"))
    if(abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and b == c):
            print("This triangle is equilateral.")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("This triangle is isosceles.")
        else:
            print("This triangle is scalene.")
    else:
        print("It doesn't specify a triangle.")
elif(number == "2"):
    a = float(input("Enter the first side:"))
    b = float(input("Enter the second side:"))
    c = float(input("Enter the third side:"))
    d = float(input("Enter the fourth side:"))
    if(a == b and b == c and c == d):
        print("This quadrilateral is square.")
    elif((a == b and c == d) or (a == c and b == d) or (a == d and b == c)):
        print("This quadrilateral is a rectangle.")
    else:
        print("This quadrilateral is an ordinary quadrilateral.")
