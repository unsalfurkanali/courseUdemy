class remoteController():
    def __init__(self, state = "Off", sound = 15, channelList = ["TRT", "Fox", "FBTV"]):
        self.state = state
        self.sound = sound
        self.channelList = channelList
        self.currentChannel = self.channelList[0]
        self.currentQueue = 0
        print("TV is ready..")
    
    def __str__(self):
        return "TV State: {}\nCurrent Channel: {} - {}\nSound: {}".format(self.state,
        self.currentQueue+1, self.currentChannel, self.sound)

    def turnOn(self):
        self.state = "On"
        print("TV turns on..")
    
    def turnOff(self):
        self.state = "Off"
        print("TV turns off..")

    def appendChannel(self, newChannel):
        self.channelList.append(newChannel.upper())
        print("Channel appended to the list..")

    def removeChannel(self, channelName):
        for i in range(len(self.channelList)):
            if channelName.lower() == self.channelList[i].lower():
                print("Removed the {}..".format(self.channelList[i]))
                self.channelList.pop(i)
                return True
        print("Failed! Not found the channel name..")
    def soundSetting(self, command):
        if command == '<':
            if not self.sound == 0:
                self.sound -= 1
        if command == '>':
            if not self.sound == 32:
                self.sound += 1
        print("Sound: {}".format(self.sound))
    
    def channelSetting(self, command):
        if len(self.channelList) == 0:
            print("There is no channel..")
            return False
        if command == "8":
            self.currentQueue += 1
            if abs(self.currentQueue) >= len(self.channelList):
                self.currentQueue = 0
            self.currentChannel = self.channelList[self.currentQueue]
        elif command == "2":
            self.currentQueue -= 1
            if abs(self.currentQueue) >= len(self.channelList):
                self.currentQueue = 0
            self.currentChannel = self.channelList[self.currentQueue]
        print("Current CH: {}".format(self.currentChannel))
    
    def settings(self):
        print("***Settings Menu***")
        print("-------------------")
        print("1-Add a channel")
        print("2-Remove a channel")
        print("3-Reset default setting")
        choice = input("Your choice: ")
        if choice == "1":
            channel = input("Enter the channel name you want to add: ")
            self.appendChannel(channel)
        elif choice == "2":
            channel = input("Enter the channel name you want to remove: ")
            self.removeChannel(channel)

rem = remoteController()
print(rem)

print("--------------------")
while True:
    command = input("Choice: ")
    if command == "1":
        rem.turnOn()
    if rem.state == "On":
        if command == ">" or command == "<":
            rem.soundSetting(command)
        elif command == "8" or command == "2":
            rem.channelSetting(command)
        elif command == "5":
            rem.settings()
        elif command == "3":
            rem.turnOff()
    elif rem.state == "Off":
        print("TV is off. Please press the '1' and turn on the TV")
    


