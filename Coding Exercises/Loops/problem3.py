"""
Try to print a multiplication table with numbers from 1 to 10.
"""

for i in range(1,11):
    print("*******************************************")
    for k in range(1,11):
        print("{} x {} = {}".format(i,k,i*k))
