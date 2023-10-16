import cv2
import numpy as np


resim = cv2.imread("3.png",0)

cv2.imshow("Gelecek",resim)
cv2.imwrite("Bizimdir.png",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()