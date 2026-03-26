import rollButton
import resetButton


userPinPath = "userPin.txt"
userPointsPath = "userPoint.txt"

##setup 
userPinList = []
userPointsList = []
userPointListInt = []

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
                userPointsList.append("1000")
                break


    elif UserInput in userPinList:
        print("\033c", end="")
        arrayPosPoint = userPinList.index(UserInput)
        loginState = False
   
    elif UserInput != 'n':
        print("Wrong pin info, please insert a valid pin or create a new account")


    
    


## Game menu
GameState = True
cost = 250
buttonWait = True
pastWin = 0
totalWinnings = 0 
while GameState:
    print("Welcome to the Widener Slot Machine!")
    print("Current Cash Amount: " , userPointsList[arrayPosPoint])
    print("Current cost: " , cost)
    print("Previous Winning Amount: ",pastWin)
    print("Total winnings: ", totalWinnings)
    char = input("Would you like to play? (y/n)")
    
    if char == "y":
        print("Please press the red button to spin!")       
        while buttonWait:
            if rollButton.state() == True:
                if int(userPointsList[arrayPosPoint]) >= cost:
                    userPointsList[arrayPosPoint] = str(int(userPointsList[arrayPosPoint]) - cost)
                    rndNum = rollButton.rollCommand()
                    point = rollButton.scoreCalc(rndNum)
                    userPointsList[arrayPosPoint] = str(int(userPointsList[arrayPosPoint]) + point)
                    pastWin = point
                    totalWinnings = totalWinnings + point
                buttonWait = False

            if resetButton.state() == True:
                resetButton.giveBack()
                buttonWait = False

    elif char == "n":
        break
    buttonWait = True
    print("\033c", end="")                
        
        
print("Thank you for playing!")




with open("userPin.txt","r+") as file:
    data = file.read()
    file.seek(0)
    file.truncate()
    for i in range(len(userPinList)):
        file.write(str(userPinList[i])+"\n")

with open("userPoint.txt","r+") as file:
    data = file.read()
    file.seek(0)
    file.truncate()
    for i in range(len(userPointsList)):
        file.write(str(userPointsList[i])+"\n")


