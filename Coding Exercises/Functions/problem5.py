"""
Write a function that prints the numbers from 1 to 100 forming a pythagorean triangle.(a <= 100,b <= 100)
"""

def find_pythagoras():
    pythagoras_list = list()

    for i in range(1,101):
        for j in range(1,101):
            c = (i ** 2 + j ** 2) ** 0.5
            if(c == int(c)):
                pythagoras_list.append((i,j,int(c)))

    return pythagoras_list

for i in find_pythagoras():
    print(i)
