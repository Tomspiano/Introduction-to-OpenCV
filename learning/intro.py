import cv2

img = cv2.imread('./pic/cat1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('cat', img)
cv2.waitKeyEx()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

cv2.imwrite('./pic/cat1gray.png', img)
