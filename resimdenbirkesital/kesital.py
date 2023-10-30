import cv2
import numpy as np

pcb= cv2.imread("pcb-kart.jpg")

kesit=pcb[50:150,300:400]
cv2.imshow("kesit alani",kesit)

pcb[0:100,0:100]=kesit
pcb[:,:,2]=222
kesit[:,:,1]=111
kesit[:,:,0]=111
pcb[333:355,333:355]=(0,111,222)
cv2.imshow("PCB Tasarim",pcb)

cv2.waitKey(0)
cv2.destroyAllWindows()