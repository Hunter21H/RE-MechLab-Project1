import RPi.GPIO as GPIO

pin = 18

def Resetsetup():
    GPIO.setmode


def state():
    if GPIO.input(pin) == GPIO.LOW:
        return True
    else:
        return False
    
def giveBack():
    return 250