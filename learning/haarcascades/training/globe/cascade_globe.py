import cv2

globe_cascades = cv2.CascadeClassifier('cascade_globe.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    globes = globe_cascades.detectMultiScale(gray, minNeighbors=30, minSize=(100, 100))
    for (x, y, w, h) in globes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        cv2.putText(img, 'globe', (x, y - h//5), font, 2, (0, 0, 225), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
