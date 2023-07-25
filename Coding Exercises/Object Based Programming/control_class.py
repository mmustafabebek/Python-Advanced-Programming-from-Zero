import random
import time

class Control():

    def __init__(self,tv_status = "Off",tv_volume = 0,channel_list = ["Trt"],channel = "Trt"):
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel = channel

    def tv_turnon(self):
        if(self.tv_status == "On"):
            print("TV is already on....")
        else:
            print("TV is turning on....")
            self.tv_status = "On"

    def tv_turnoff(self):
        if(self.tv_status == "Off"):
            print("TV is already off....")
        else:
            print("TV is turning off....")
            self.tv_status = "Off"

    def volume_settings(self):
        while True:
            answer = input("Turn down the volume: '<'\nTurn up the volume: '>'\nExit: 'Exit'\n")

            if(answer == "<"):
                if(self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("Volume:",self.tv_volume)
            elif(answer == ">"):
                if(self.tv_volume != 31):
                    self.tv_volume += 1
                    print("Volume:",self.tv_volume)
            else:
                print("Volume has been uptaded:",self.tv_volume)
                break

    def add_channel(self,channel_name):
        print("Adding channel....")
        time.sleep(1)

        self.channel_list.append(channel_name)
        print("Channel has been added....")

    def random_channel(self):
        randomm = random.randint(0,len(self.channel_list)-1)
        self.channel = self.channel_list[randomm]
        print("Current Channel:",self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV Status: {}\nTV Volume: {}\nChannel List: {}\nCurrent Channel: {}\n".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)


control = Control()

print("""

Television Application

1. Turn on the TV

2. Turn off the TV

3. Volume Settings

4. Add Channel

5. Find out the number of channels

6. Random Channel

7. TV Information

Press 'q' to exit
""")

while True:

    transaction = input("Choose a transaction:")
    if(transaction == "q"):
        print("Program is shutting down....")
        break
    elif(transaction == "1"):
        control.tv_turnon()
    elif(transaction == "2"):
        control.tv_turnoff()
    elif(transaction == "3"):
        control.volume_settings()
    elif(transaction == "4"):
        channel_names = input("Enter the channel names to be added to the TV (seperate with commas):")
        channel_list = channel_names.split(",")
        for will_be_added in channel_list:
            control.add_channel(will_be_added)
    elif(transaction == "5"):
        print("Number of channels:",len(control))
    elif(transaction == "6"):
        control.random_channel()
    elif(transaction == "7"):
        print(control)
    else:
        print("Invalid transaction....")
