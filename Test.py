import cv2
import numpy as np
import pytesseract 
#PROGRAM TO SEPARATE OUT A CHARACTER FROM A GIVEN IMAGE USING SIMPLE METHODS LIKE OPTICAL CHARARCTER RECOGNITION AND MASKING TECHNIQUES.
#DEVELOPED BY ANUBHAV MISHRA

#Reading the image
inimage=cv2.imread("Test_images/1.jpeg")
cv2.imshow("output",inimage)
cv2.waitKey(0)

