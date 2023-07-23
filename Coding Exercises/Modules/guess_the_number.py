import random
import time

print("""***************************************

Number Guessing Game


Guess the number between 1 and 40.


***************************************""")

random_number = random.randint(1,40)
guess_right = 7
while True:

    guess = int(input("Your guess:"))

    if(guess < random_number):
        print("Information Queries...")
        time.sleep(1)

        print("Say a higher number....")

        guess_right -= 1
    elif(guess > random_number):
        print("Information Queries...")
        time.sleep(1)

        print("Say a lower number....")

        guess_right -= 1
    else:
        print("Information Queries....")
        time.sleep(1)
        print("Congratulations! Our number",random_number)
        break

    if(guess_right == 0):
        print("Your Guess Is Over...")
        print("Your number:",random_number)
        break
