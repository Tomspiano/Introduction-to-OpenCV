import cv2

img1 = cv2.imread('./picture/universe.jpg')
img2 = cv2.imread('./picture/wolf1.jpg')

rows1, cols1, channels1 = img1.shape
rows2, cols2, channels2 = img2.shape
roi = img1[rows1 - rows2:rows1, 0:cols2]
# print(roi.shape[:2], img1.shape[:2], img2.shape[:2])
# cv2.imshow('roi', roi)
# cv2.waitKeyEx()

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img2gray, 225, 255, cv2.THRESH_BINARY_INV)
# print(mask)
# cv2.imshow('mask', mask)
# cv2.waitKeyEx()

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[rows1 - rows2:rows1, 0:cols2] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img_bg', img1_bg)
cv2.imshow('img_fg', img2_fg)
cv2.imshow('dst', dst)

cv2.waitKeyEx()
