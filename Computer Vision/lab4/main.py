import cv2
import numpy as np
from matplotlib import pyplot as plt

def threshold(img, threshold):
    result = img.copy()

    for i in range(result.size):

        pixel = result.item(i)

        if pixel > threshold:
            result.itemset(i, 255)
        else:
            result.itemset(i, 0)
    
    return result

def task2(name):  
    img = cv2.imread(name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
    ret,thresh6 = cv2.threshold(gray,250,120,cv2.THRESH_OTSU)
    ret,thresh7 = cv2.threshold(gray,127,255,cv2.THRESH_TRIANGLE)

    cv2.imshow("Task ot", thresh6)
    # cv2.imshow("Task t", thresh4)
    # cv2.imshow("Task tu", thresh5)
    cv2.waitKey(0)

    thresh8 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 55, -25)

    thresh9 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, -25)


    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'THR_OTSU', 'THR_TRIANGLE', 'ADAPT_THR_MEAN_C', 'ADAPT_THR_GAUSSIAN_C']
    images = [gray, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, thresh8, thresh9]

    # for i in range(10):
    #     plt.subplot(3,4,i+1),plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    # plt.show()

img = cv2.imread("asd.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = threshold(gray, 220)

cv2.imshow("Task 1", result)
cv2.waitKey(0)

task2("asd.png")
# task2("asd.png")
# task2("asd.png")