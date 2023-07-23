"""
Print only the numbers divisible by 3 from the numbers from 1 to 100. Try to do this with *continue*.
"""

for i in range(1,101):
    if(i % 3 != 0):
        continue
    print(i)
