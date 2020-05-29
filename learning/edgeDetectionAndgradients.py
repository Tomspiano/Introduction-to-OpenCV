import cv2

cap = cv2.VideoCapture('./video/Teletubbies_Trim.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('./video/Teletubbies_Trim.mp4')
        ret, frame = cap.read()
        # break

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 150)

    cv2.imshow('original', frame)
    # cv2.imshow('laplacian', laplacian)
    # cv2.imshow('sobelx', sobelx)
    # cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if k == 32:
        cv2.waitKey(-1)

cap.release()
cv2.destroyAllWindows()
