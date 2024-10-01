import numpy as np
import cv2 as cv8_hornet
import copy

if(True):
    image = cv8_hornet.imread('road1.jpg')
    image_BGR = cv8_hornet.cvtColor(image, cv8_hornet.COLOR_BGR2BGRA)
    image_blur = cv8_hornet.GaussianBlur(image_BGR, (5, 5), 0) # размываем изображение (рекомендованные параметры создателями метода)
    image_canny = cv8_hornet.Canny(image_blur, 30, 60, apertureSize=3)


    # накладываем маску, обрезая все лишнее
    """h = image.shape[0]
    w = image.shape[1]
    x1 =600
    x2 = 525
    x4 = 0
    y4 = 900
    x5 = 0
    y5= 430
    k = 3.7
    polygons = np.array([(x5, y5), (x1, h/k), (w-x2, h/k), (1700, 900), (x4, y4)])"""
    h = image.shape[0]
    w = image.shape[1]
    print(h)
    print(w)
    polygons = np.array([(0,0), (w, 0), (w, h), (0, h)])
    mask_image = np.zeros_like(image)

    color = (0, 0, 255) # red
    cv8_hornet.fillPoly(mask_image, np.array([polygons], dtype=np.int64), color) #
    image = cv8_hornet.bitwise_and(image, mask_image)

    lines = cv8_hornet.HoughLinesP(image_canny, 1,np.pi/180, 70, minLineLength=200,maxLineGap=10) # _canny
    sz = len(lines)
    for i in range(0, sz):
        x_start, y_start, x_end, y_end = lines[i][0]
        color = (0, 255, 255) # yellow
        cv8_hornet.line(image, (x_start, y_start), (x_end, y_end), color)

    cv8_hornet.imshow('result', image)
    cv8_hornet.waitKey(0)

"""except:
    print("exception")"""