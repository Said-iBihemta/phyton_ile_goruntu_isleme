import cv2
import numpy as np

kare=cv2.imread("i.jpg")

cv2.rectangle(kare,(55,61),(88,111),[0,0,255],2)
cv2.imshow("Ustad",kare)
cv2.imwrite("ustad.jpg",kare)


cv2.waitKey(0)
cv2.destroyAllWindows()