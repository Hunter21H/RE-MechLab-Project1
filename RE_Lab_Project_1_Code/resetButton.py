import RPi.GPIO as GPIO

pin = 18
GPIO.setmode(GPIO.BOARD)

def Resetsetup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def state():
    if GPIO.input(pin) == GPIO.HIGH:
        return True
    else:
        return False
    
def giveBack():
    return 250
