import cv2
import numpy as np

cap = cv2.VideoCapture('./video/Teletubbies_Trim.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('./video/Teletubbies_Trim.mp4')
        ret, frame = cap.read()
        # break
    cv2.imshow('frame', frame)

    # color filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv hue sat value
    lower_purple = np.array([50, 0, 40])
    upper_purple = np.array([170, 80, 120])

    mask = cv2.inRange(frame, lower_purple, upper_purple)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    kernel = np.ones((10, 10), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if k == 32:
        cv2.waitKey(-1)

cap.release()
cv2.destroyAllWindows()
