import RPi.GPIO as GPIO
import serial 

pin = 16
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)

## Gets the number of the matched numbers and returns points earned 
def pointMatch(x):
        match x:
            case 0:
                return 0
            case 1:
                return 150
            case 2:
                return 250
            case 3:
                return 350
            case 4:
                return 450
            case 5:
                return 550
            case 6:
                return 650
            case 7:
                return 750
            case 8:
                return 850
            case 9:
                return 950

def Rollsetup():
    GPIO.setmode


def state():
    if GPIO.input(pin) == GPIO.LOW:
        return True
    else:
        return False
    

def rollCommand():
    ser.write(b"r\n")
    return UnoListener()

#returns numbers the uno generated into a 
def UnoListener():
    msg = ser.readline().decode('utf-8').rstrip
    msgArray = msg.split(',')
    num = int(msgArray)
    return num
    

def scoreCalc(num):
    
    

    x1 = num[0]
    x2 = num[1]
    x3 = num[2]
    x4 = num[4]
    xArray = [x1,x2,x3,x4]
    sum = x1 + x2 + x3 + x4
    #4 match
    if sum/x1 == 4:
        return pointMatch(x1) * 100
    
    #checks for pairs
    list1 = [] # first set of pairs
    list2 = [] # second set of pairs
    list3 = [] # for numbers that have no matches
    for i in range(len(xArray)):
        if(i == 0): list1.append(xArray[i])

        if(xArray[i] == list1[i-1]):
            
            list1.append(xArray[i])
        
        elif(xArray[i] == list2[i-1]):
            
            list2.append(xArray[i])
        
        else:
            list3.append(xArray[i])

    if (len(list1) > 1): pointMatch(list1[0])
    if (len(list2) > 1): pointMatch(list2[0])



#             I love gambling
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⠛⠛⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⠀⣷⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀⠀
# ⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀⠀⠀
# ⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀⠀⠀
# ⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
# ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
# ⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀