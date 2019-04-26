#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[6]:


#Get the reference to our Webcam
#create a VideoCapture object
#Normally one camera will be connected. So I simply pass 0
#You can select the second camera by passing 1

WebCam=cv2.VideoCapture(0)


while(True):
    #reading a new frame
    
    #"Frame" will get the next frame in the camera. 
    #"Ret" will obtain return value from getting the camera frame, either true of false
    
    ret,frame=WebCam.read()
    
    #show the frame
    cv2.imshow("New Frame", frame)
    
    #exit the camera if a key pressed(here it is the letter 'q')
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
       
    
    
WebCam.release()
cv2.destroyAllWindows()
    


# In[7]:


# get the reference to the webcam
WebCam2 = cv2.VideoCapture(0)
HEIGHT = 500

while(True):
    # read a new frame
    _, frame = WebCam2.read()
    
    # flip the frame
    frame = cv2.flip(frame, 1)
    

    # add rectangle
    cv2.rectangle(frame, (250, 75), (500, 375), (0, 0, 255), 4)

    # show the frame
    cv2.imshow("Capturing frames", frame)

    # quit camera if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

WebCam2.release()
cv2.destroyAllWindows()
    


# In[14]:


#Save a picture when clicking S key


# In[5]:


WebCam3 = cv2.VideoCapture(0)
HEIGHT = 500
FrameArray = []

while(True):
    # read a new frame
    ret, frame = WebCam3.read()
    
    # flip the frame
    frame = cv2.flip(frame, 1)


    # add rectangle
    cv2.rectangle(frame, (250, 75), (500, 375), (0, 255, 0), 4)

    # show the frame
    cv2.imshow("Capturing frames", frame)

    key = cv2.waitKey(1)

    # quit camera if 'q' key is pressed
    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("s"):
        # save the frame
        
        roi = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FrameArray.append(roi)
        
        # preview the frame
        plt.imshow(roi)
        plt.show()

WebCam3.release()
cv2.destroyAllWindows()
        


# In[ ]:




