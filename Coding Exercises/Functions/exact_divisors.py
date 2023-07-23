def findexactdivisors(number):
    exactdivisors = []

    for i in range(2,number):
        if(number % i == 0):
            exactdivisors.append(i)
    return exactdivisors

while True:

    number = input("Number:")

    if(number == "q"):
        print("Program Terminating")
        break
    else:
        number = int(number)
        print("Exact Divisors:",findexactdivisors(number))
