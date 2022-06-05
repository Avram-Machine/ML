import cv2
import numpy as np

img = cv2.imread("6_1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = cv2.bitwise_not(gray)

# Biggest line
lines = cv2.HoughLinesP(invert,7,np.pi/720,400,minLineLength=160,maxLineGap=75)

if lines is not None:
    maxlen = 0
    for line in lines:
        x1,y1,x2,y2 = line[0]
        curlen = (abs(x1 - x2)**2 + abs(y1 - y2)**2)**(1/2)
        if curlen > maxlen:
            maxlen = curlen
            biggestLine = line

    x1,y1,x2,y2 = biggestLine[0]
    cv2.line(img,(x1,y1),(x2,y2),(88,255,188),5)

# Biggest circle
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,4,300,param1=300,param2=500,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

maxRadius = 0
for i in circles[0,:]:
    if i[2] > maxRadius:
        maxRadius = i[2]
        biggestCircle = i

# draw the outer circle
cv2.circle(img,(biggestCircle[0],biggestCircle[1]),biggestCircle[2],(88,255,188),5)

cv2.imwrite("6_1_done.png", img)

img = cv2.imread("6_2.png")

edges = cv2.Canny(img,120,150,apertureSize = 7)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

if lines is not None:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a*rho
        y0 = b*rho

        x1 = int(x0 + 2000*(-b))
        y1 = int(y0 + 2000*(a))
        x2 = int(x0 - 2000*(-b))
        y2 = int(y0 - 2000*(a))

        cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 25)

cv2.imwrite("6_2_done.png", img)