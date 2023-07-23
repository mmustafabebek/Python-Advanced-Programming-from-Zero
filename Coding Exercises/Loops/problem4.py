"""
In each while loop, take a number from the user and add the numbers entered by the user to a variable named "sum".
When the user presses the "q" key, terminate the loop and print the "sum variable" to the screen.
"""

total = 0

while True:
    number = input("Enter a number:")
    if(number == "q"):
        break
    number = int(number)

    total += number
print("Sum of entered numbers: ",total)
