print(""""*************************************

Factorial Finding Program


Press q to exit. Press q to exit.
*************************************""")


while True:
    number = input("Number:")
    if(number == "q"):
        print("Program Terminating.")
        break

    else:
        number = int(number)

        factorial = 1

        for i in range(2,number+1):
            print("Factorial",factorial,"i:",i)
            factorial *= i
        print("Factorial ",factorial)