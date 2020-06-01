import cv2

smile_cascades = cv2.CascadeClassifier('haarcascade_smile.xml')

lefteye_cascades = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

righteye_cascades = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = smile_cascades.detectMultiScale(gray, 1.5, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        lefteyes = lefteye_cascades.detectMultiScale(roi_gray)
        righteyes = righteye_cascades.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in lefteyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 225, 0), 2)
        for (ex, ey, ew, eh) in righteyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 225), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
