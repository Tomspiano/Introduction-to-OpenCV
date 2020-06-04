import cv2

path = input('path: ')  # pen.jpg
w = eval(input('width: '))  # 50
h = eval(input('height: '))  # 50
size = (w, h)

img = cv2.imread(path)
resized = cv2.resize(img, size)
cv2.imwrite(path, resized)
