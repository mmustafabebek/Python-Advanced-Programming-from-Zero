"""
Get information about how much a vehicle has burned per kilometer and how many kilometers it has traveled, and calculate
how much the driver must pay in total.
"""

burningperkm = float(input("The amount the vehicle burns per kilometer:"))
kmroad = int(input("The distance traveled by the vehicle in km:"))

print("Amount: {} tl".format(burningperkm * kmroad))