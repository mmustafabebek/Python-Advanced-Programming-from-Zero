"""
Have a list like this.

[1,2,3,4,5,6,7,8,9,10]

Write a function that prints the sum of the even numbers in this list.
Note: First remove the even numbers with the filter() function. Then use the reduce() function.

"""

from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]

def even(x):
    if(x % 2 == 0):
        return x
    else:
        pass

filter1 = list(filter(even,list1))

def collection(x,y):
    return x + y

print(reduce(collection,filter1))
