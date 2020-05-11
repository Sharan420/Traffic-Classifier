# ======================================================
# Thrown together by Sharan And Aditya
# DO NOT PLAGARISE
# DON'T
# ======================================================


import cv2
import socket
import numpy as np
from PIL import Image
from tensorflow.keras import models
import matplotlib.pyplot as plt

#Creating the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# get local machine name
host = socket.gethostname()

port = 4345

# connection to hostname on the port.
s.connect((host, port))

#Loading lists HIGH and LOW
HIGH = []
LOW = []

#Loading the model
model = models.load_model('keras_model.h5')
#Initialising The webcam
video = cv2.VideoCapture(0)

for i in range(100):
        _, frame = video.read()
        
        im = Image.fromarray(frame, 'RGB')

        #Resizing the array
        im = im.resize((224,224))
        #Converting into Numpy array again
        img_array = np.array(im)

         
        img_array = np.expand_dims(img_array, axis=0)

        #Calling the predict() function 
        prediction = model.predict(img_array)[0][0]
        pper = prediction * 100
        HIGH.append(pper)
        prediction2 = model.predict(img_array)[0][1]
        pper2 = prediction2 * 100
        LOW.append(pper2) 

       # Unncomment to see result to each run 
       # print("HIGH: ",round(pper,2),"%","LOW: ",round(pper2,2),"%")

       

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()

#Initialising the variables which would contain the average values
HIGH_av = 0
LOW_av = 0

#Calculating the average value for HIGH prediction
for j in range(0,len(HIGH)):
    HIGH_av += HIGH[j]
for k in range(0,len(LOW)):
    LOW_av += LOW[k]

HIGH_av = HIGH_av/100
LOW_av = LOW_av/100

#Printing the average values
print('HIGH%: ',HIGH_av,'LOW%: ',LOW_av)
fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
ptage = ['LOW','HIGH']
value = [LOW_av,HIGH_av]
y_pos = np.arange(len(ptage))
plt.bar(y_pos,value,align='center', alpha=0.5)
plt.xlabel('categories')
plt.ylabel('values')
plt.xticks(y_pos, ptage)
plt.show(block=True)

s.send(str(HIGH_av).encode('ascii'))
s.close()
