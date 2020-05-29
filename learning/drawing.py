import cv2
import numpy as np

img = cv2.imread('./picture/dog1.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (10, 10), (150, 150), (0, 0, 0), 10)
cv2.rectangle(img, (15, 15), (200, 200), (0, 255, 0), 5)
cv2.circle(img, (100, 150), 50, (255, 0, 0), -1)

pts = np.array([[10, 5], [100, 80], [70, 20], [80, 15]], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255), 2)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Hello OpenCV', (100, 400), font, 1, (255, 150, 200), 2, cv2.LINE_8)

cv2.imshow('dog', img)
cv2.waitKeyEx()
