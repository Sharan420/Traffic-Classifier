import cv2
import numpy as np
from PIL import Image
from tensorflow.keras import models

#Load the saved model
model = models.load_model('/Users/sharansuri/Desktop/IMAGE/keras_model.h5')
video = cv2.VideoCapture(0)

for i in range(100):
        _, frame = video.read()
        
        im = Image.fromarray(frame, 'RGB')

        
        im = im.resize((224,224))
        img_array = np.array(im)

         
        img_array = np.expand_dims(img_array, axis=0)

        
        prediction = model.predict(img_array)[0][0]
        pper = prediction * 100
        prediction2 = model.predict(img_array)[0][1]
        pper2 = prediction2 * 100
        print("HIGH: ",round(pper,2),"%","LOW: ",round(pper2,2),"%")

       

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
