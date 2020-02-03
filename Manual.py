import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT, initial=gpio.LOW)
gpio.setup(38, gpio.OUT, initial=gpio.LOW)
gpio.setup(36, gpio.OUT, initial=gpio.LOW)

def REDL():
    gpio.output(38, False)
    gpio.output(36,False)
    gpio.output(40, True)
def GRNL():
    gpio.output(40, False)
    gpio.output(38,False)
    gpio.output(36, True)
def YWL():
    gpio.output(40,False)
    gpio.output(36,False)
    gpio.output(38, True)

while True:
    print("Enter the wanted state \n 1.RED 2.Yellow 3.GREEN 4.OFF")
    a1 = input(":")
    if a1 in "1REDredR":
        REDL()
    elif a1 in "2YELLOWyellowY":
        YWL()
    elif a1 in "3GREENgreenG":
        GRNL()
    else:
        gpio.output(36,False)
        gpio.output(38,False)
        gpio.output(40,False)
        exit()
