import numpy as np
import sys
import cv2
dir= sys.argv[1]
file = sys.argv[2]
filename= dir+"/"+file+".avi"

cap = cv2.VideoCapture(1)

# Define the codec and create VideoWriter object
#fourcc = cv2.FOURCC(*'')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, -1)
        #write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

