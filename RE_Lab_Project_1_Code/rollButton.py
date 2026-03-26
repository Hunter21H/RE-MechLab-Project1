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
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


def state():
    if GPIO.input(pin) == GPIO.HIGH:
        return True
    else:
        return False
    

def rollCommand():
    ser.write(b"r\n")
    msg = UnoListener()
    return msg
   

#returns numbers the uno generated into a 
def UnoListener():
    while True:
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').strip()
            msgArray = msg.split(',')
            num = []
            for i in range(len(msgArray)):
                num.append(int(msgArray[i]))
            
            return num
    

def scoreCalc(num):
    
    

    x1 = num[0]
    x2 = num[1]
    x3 = num[2]
    x4 = num[3]
    xArray = [x1,x2,x3,x4]
    total = x1 + x2 + x3 + x4
    finalPoint = 0
    
    #4 match
    if total/x1 == 4:
        return pointMatch(x1) * 100
    
    #checks for pairs
    list1 = [] # first set of pairs
    list2 = [] # second set of pairs
    list3 = [] # for numbers that have no matches
  
    for i in range(len(xArray)):
        if(i == 0): list1.append(xArray[i])

        
        elif(i == 1):
            if (xArray[i] in list1):
                
                list1.append(xArray[i])
            else:
                list2.append(xArray[i])
        elif(i>=2):
       
            if (xArray[i] in list1):
                    list1.append(xArray[i])
            elif(xArray[i] in list2):
                    list2.append(xArray[i])
            else:
                    list3.append(xArray[i])
    print("Length of list 1: ", len(list1))
    print("Length of list 2: ", len(list2))
    
    if (len(list1) > 1): 
        print("Value for list 1: ",pointMatch(list1[0]))
        finalPoint = finalPoint+pointMatch(list1[0])
    if (len(list2) > 1): 
        print("Value for list 2: ",pointMatch(list2[0]))
        finalPoint = finalPoint+pointMatch(list2[0])
    return finalPoint


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
