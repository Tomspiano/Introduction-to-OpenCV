import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./picture/dog1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (80, 10, 260, 215)
# cv2.rectangle(img, (80,10),(260,215), (255,0,0), 1)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.colorbar()
plt.show()
