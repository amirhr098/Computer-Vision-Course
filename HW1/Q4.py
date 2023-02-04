from time import sleep
import cv2
image = cv2.imread('background.png', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('image',mat=image)
image = cv2.resize(image, (570, 290))
image = cv2.line(image, (5,5),(565,5),(0,0,0),1)
cv2.imshow('image',mat=image)
sleep(10)