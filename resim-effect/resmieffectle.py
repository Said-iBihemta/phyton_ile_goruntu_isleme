import cv2
import numpy as np

pcb=cv2.imread("kart-tasarim.jpg")
pcb[30:50,60:90,0]=255
pcb[:,:,1]=111
pcb[:,:,2]=111


cv2.imshow("PCB Tasarim",pcb)



cv2.waitKey(0)
cv2.destroyAllWindows()



