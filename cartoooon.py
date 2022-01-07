import numpy as np
import cv2

cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

shift = 5

while(True):
    ret, frame = cap.read()
    
    epf = cv2.edgePreservingFilter(frame, flags=cv2.NORMCONV_FILTER)
    basetoon = cv2.stylization(epf, sigma_s=199, sigma_r=0.01)
    basetoon = ((basetoon[:,:,[0,1,2]] >> shift)) << shift

    cv2.imshow('EPF', basetoon)

    #'p' saves a copy
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("testpic.jpg",basetoon)
        
    #'q' quits 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()