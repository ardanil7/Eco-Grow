# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:52:07 2023

@author: ardaf
"""

import cv2

# create a video capture object
cap = cv2.VideoCapture(0)

# loop through frames from the camera
while True:
    # read a frame from the camera
    ret, frame = cap.read()

    # check if the frame was successfully read
    if not ret:
        print("Error reading frame")
        break

    # do some processing on the frame
    # for example, convert it to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the processed frame
    cv2.imshow("Processed Frame", gray_frame)

    # wait for a key press
    key = cv2.waitKey(1)

    # if the 'q' key is pressed, break the loop
    if key == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()