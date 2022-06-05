import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Task 1
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Флаг для перевода изображения в чернобелое
cv2.imwrite("grayscale_image.jpg", gray)

cv2.imshow("RGB", img)
cv2.imshow("GRAYSCALE", gray)
cv2.waitKey(0)

# Task 2
invert = cv2.bitwise_not(gray)

cv2.imshow("GRAYSCALE INVERTED", invert)
cv2.waitKey(0)

# Task 3
red = img[:,:,2]
green = img[:,:,1]

colorswap = img.copy()

colorswap[:,:,1] = red
colorswap[:,:,2] = green

cv2.imshow("SWAP RG CHANNELS", colorswap)
cv2.waitKey(0)

# Extra task 1
height = 600
width = 800
blank_image = np.zeros((height,width,3), np.uint8)  

blank_image[0:height//3,:] = (255,255,255) # (B, G, R)
blank_image[height//3:(height//3)*2,:] = (255,0,0)
blank_image[(height//3)*2:height,:] = (0,0,255)

cv2.imshow("EXTRA TASK 1", blank_image)
cv2.waitKey(0)