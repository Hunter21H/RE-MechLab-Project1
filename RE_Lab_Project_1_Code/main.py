import rollButton
import resetButton
import keyboard


userPinPath = "userPin.txt"
userPointsPath = "userPoint.txt"

##setup 
userPinList = []
userPointsList = []

rollButton.Rollsetup()
resetButton.Resetsetup()

with open(userPinPath, 'r') as file:
    for line in file:
        userPinList.append(line.strip())
        
with open(userPointsPath, 'r') as file:
    for line in file:
        userPointsList.append(line.strip())
    
## User Login
loginState = True
arrayPosPoint = 0

while loginState:

    print("Please enter user pin")
    print("Or type n to make a new pin")

    UserInput = input()

    if UserInput == 'n':
        while True:
            newPin = input("Please input a new pin: ")

            if newPin in userPinList:
                print("Ths pin is already being used please make a new pin")
                print("\033c", end="")
            else:
                print("New pin create, thank you")
                userPinList.append(newPin)
                userPointsList.append("10000")
                break


    if UserInput not in userPinList:
        print("Wrong pin info, please insert a valid pin or create a new account")
    else:
        print("\033c", end="")
        arrayPosPoint = userPinList.index(UserInput)
        loginState = False

## Game menu
GameState = True
cost = 250
buttonWait = True
endProgram = False
while GameState:
    print("Welcome to the Widener Slot Machine!")
    print("Current Cash Amount: " + userPointsList[arrayPosPoint])
    print("Current cost: " + cost)
    print("Please press the yellow button to spin!")
    print("When done please press Q to finish program")
    
    while buttonWait:
        if rollButton.state() == True:
            if userPointsList[arrayPosPoint] >= cost:
                userPointsList[arrayPosPoint] = userPointsList[arrayPosPoint] - cost
                rndNum = rollButton.rollCommand()
                userPointsList[arrayPosPoint] = userPointsList[arrayPosPoint] + rollButton.scoreCalc(rndNum)
            buttonWait = False

        if resetButton.state() == True:
            resetButton.giveBack()
            buttonWait = False

        if keyboard.is_pressed("q"):
                endProgram = True
    if endProgram == True:
        break
    else:
        buttonWait = True
        print("\033c", end="")

with open("userPin.txt","r+") as file:
    data = file.read()
    file.seek(0)
    file.truncate()
    for i in range(len(userPinList)):
        file.write(userPinList[i],"/n")

with open("userPoint.txt","r+") as file:
    data = file.read()
    file.seek(0)
    file.truncate()
    for i in range(len(userPointsList)):
        file.write(userPointsList[i],"/n")


