# the transformations include
# color filtering, blurring and smoothing
import cv2
import numpy as np

cap = cv2.VideoCapture('./video/Teletubbies_Trim.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
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

    # removing noise
    # smoothing
    # kernel = np.ones((15, 15), np.float) / 255
    # smoothed = cv2.filter2D(res, -1, kernel)
    # cv2.imshow('smoothed', smoothed)

    # blurring
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
