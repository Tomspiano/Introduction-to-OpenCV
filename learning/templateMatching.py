import cv2
import numpy as np

img_bgr = cv2.imread('./picture/messy.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

n = 3
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
while n:
    template = cv2.imread('./picture/template' + str(n) + '.jpg')
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[:2]

    res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    n = n - 1

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), color[n], 1)

cv2.imshow('detected', img_bgr)
cv2.waitKeyEx()
