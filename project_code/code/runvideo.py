import cv2
import sys
import time

dir= sys.argv[1]
file = sys.argv[2]
filename= dir+"/"+file+".avi"
filename= filename[1:]

cap = cv2.VideoCapture(filename)
time.sleep(0.8)
while True:
    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
