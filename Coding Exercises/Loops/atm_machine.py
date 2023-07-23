print("""***************************************

Welcome to ATM Machine

Transactions;

1. Balance Inquiry

2. Deposit Money

3. Withdraw Money

Press 'q' to exit the program.
***************************************
""")

balance = 1000

while True:
    transaction = input("Select the action:")

    if(transaction == "q"):
        print("We are waiting for you again")
        break
    elif(transaction == "1"):
        print("Your balance is {} tl".format(balance))
    elif(transaction == "2"):
        amount = int(input("Enter the amount:"))
        balance += amount
    elif(transaction == "3"):
        amount = int(input("Enter the amount:"))
        if(amount > balance):
            print("You cannot withdraw such an amount...")
            continue
        balance -= amount
    else:
        print("Invalid Transaction...")