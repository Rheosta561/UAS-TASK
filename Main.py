import cv2
import numpy as np
# Defining a Function named as image segmentor
def image_segmentor(a):
    # Reading the Image
    image=cv2.imread(a)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Thresholding the image read 
    output1, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("The separated Character is :",threshold)
    cv2.waitKey(0)
b=True
c=1
while b==True:
    image_name="Test_images/"+str(c)+".jpeg"
    image_segmentor(image_name)
    choice=int(input("Do you want to open segment another image , 1--yes ; 2--no"))
    if choice==1:
        c+=1
        continue
    else:
        b==False



