import cv2

cap = cv2.VideoCapture('./video/Teletubbies_background.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('./video/Teletubbies_background.mp4')
        ret, frame = cap.read()
        # break
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == 32:
        cv2.waitKey(-1)

cap.release()
cv2.destroyAllWindows()
