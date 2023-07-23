print("""****************************************
Calculator Program

Transactions;

1. Addition

2. Subtraction

3. Multiplication

4. Division
****************************************
""")

transaction = input("Enter the transaction:")

a = int(input("First Number:"))
b = int(input("Second Number:"))

if (transaction == "1"):
    print("The sum of {} and {} is {} ".format(a,b,a+b))
elif (transaction == "2"):
    print("The difference of {} and {} is {} ".format(a,b,a-b))
elif (transaction == "3"):
    print("The product of {} and {} is {} ".format(a,b,a*b))
elif (transaction == "4"):
    print ("{} divided by {} is {} ".format(a,b,a/b))
else:
    print("Invalid operation!")
