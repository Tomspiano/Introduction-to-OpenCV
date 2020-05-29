import cv2

img = cv2.imread('./picture/bookpage.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval3, otsu = cv2.threshold(gray, 12, 255, cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaussian', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKeyEx()
