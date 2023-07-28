"""
Imagine creating a list of strings.

list = ["345","sadas","324a","14","kemal"]

Print the strings in this list that contain only numbers to the screen. Remember to use try,except blocks when doing this.
"""

list1 = ["345","sadas","324a","14","kemal"]

for element in list1:
    try:
        print(int(element))
    except:
        pass
print("Program terminated.")