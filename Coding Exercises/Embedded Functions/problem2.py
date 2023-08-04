"""
Let's say you have a list where each element is a tuple of 3.

[(3,4,5),(6,8,10),(3,10,7)]

Now write a function that returns whether these sides are triangles based on their side lengths, and print the list
containing only the sides that indicate triangles.

[(3, 4, 5), (6, 8, 10)]

"""

list1 = [(3,4,5),(6,8,10),(3,10,7)]


def is_it_a_triangle(tuple):
    if(abs(tuple[0] + tuple[1]) > tuple[2] and abs(tuple[0] + tuple[2]) > tuple[1] and abs(tuple[1] + tuple[2]) > tuple[0]):
        return True
    else:
        return False

print(list(filter(is_it_a_triangle,list1)))
