import time


class Computer():
    def __init__(self,status = "Off",operating_system = "Windows",processor = "Intel Core i7",ram = "8 GB",price = 20000):
        self.status = status
        self.operating_system = operating_system
        self.processor = processor
        self.ram = ram
        self.price = price

    def turn_on(self):
        if(self.status == "On"):
            print("The computer is already on....")
        else:
            print("The computer is turning on....")
            self.status = "On"

    def turn_off(self):
        if(self.status == "Off"):
            print("The computer is already off....")
        else:
            print("The computer is shutting down....")
            self.status = "Off"

    def __str__(self):
        return "Computer Status: {}\nOperating System: {}\nProcessor: {}\nRam: {}\nPrice: {}\n".format(self.status,self.operating_system,self.processor,self.ram,self.price)


computer = Computer()

print("""

Computer Application

1. Turn On the Computer

2. Shut Down the Computer

3.Computer Information 

Press 'q' to exit
""")

while True:

    transaction = input("Choose a transaction:")
    if(transaction == "q"):
        print("Exiting....")
    elif(transaction == "1"):
        time.sleep(1)
        computer.turn_on()
    elif(transaction == "2"):
        time.sleep(1)
        computer.turn_off()
    elif(transaction == "3"):
        print(computer)
    else:
        print("Invalid Transaction....")

