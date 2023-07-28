"""
Imagine creating a list of strings.

list = ["345","sadas","324a","14","kemal"]

Print the strings in this list that contain only numbers to the screen. Remember to use try,except blocks when doing this.
"""

list1 = ["345","sadas","324a","14","kemal"]

for i in list1:
    try:
        print(int(i))
    except ValueError:
        print("{} is not just data with numbers.".format(i))
print("Program terminated.")