import cv2
import socket
import numpy as np
from PIL import Image
from tensorflow.keras import models
import RPi.GPIO as gpio
from time import sleep

print("Socket successfully created")

host = "192.168.43.64"

port = 4345

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(40, gpio.OUT, initial=gpio.LOW)
gpio.setup(38, gpio.OUT, initial=gpio.LOW)
gpio.setup(36, gpio.OUT, initial=gpio.LOW)

def REDL(TME):
    gpio.output(38, False)
    gpio.output(36,False)
    gpio.output(40, True)
    sleep(TME)
    gpio.output(40, False)
def GRNL(TA):
    gpio.output(40, False)
    gpio.output(38,False)
    gpio.output(36, True)
    sleep(TA)
def YWL():
    gpio.output(40,False)
    gpio.output(36,False)
    gpio.output(38, True)
    sleep(5)

HIGH = []
LOW = []


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
    s.connect((host, port))
    model = models.load_model('keras_model.h5')
    video = cv2.VideoCapture(0)
    for i in range(10):
            _, frame = video.read()
        
            im = Image.fromarray(frame, 'RGB')

            im = im.resize((224,224))
            img_array = np.array(im)

         
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)[0][0]
            pper = prediction * 100
            HIGH.append(pper)
            prediction2 = model.predict(img_array)[0][1]
            pper2 = prediction2 * 100
            LOW.append(pper2) 


       
    video.release()
    cv2.destroyAllWindows()

    HIGH_av = 0
    LOW_av = 0

    for j in range(0,len(HIGH)):
        HIGH_av += HIGH[j]
    for k in range(0,len(LOW)):
        LOW_av += LOW[k]

    HIGH_av = HIGH_av/10
    LOW_av = LOW_av/10

    print('HIGH%: ',HIGH_av,'LOW%: ',LOW_av)
    bcd = [HIGH_av,LOW_av]
    s.send(str(bcd).encode('ascii'))
    msg = s.recv(1024)
    al = msg.decode('ascii')
    al = str(al)
    s.close()
    print(al)
    
    ti = 30
    if al == 'RED':
        ti += 15
        YWL()
        REDL(ti)
    if al == 'GREEN':
        YWL()
        GRNL(ti-10)
    HIGH_av = 0
    LOW_av = 0
    HIGH = []
    LOW = []
