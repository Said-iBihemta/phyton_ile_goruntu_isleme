import cv2
import numpy as np


resim = cv2.imread("Bizimdir.png")

cv2.imshow("Bizimdir.png",resim)
print(resim.size)
print(resim.dtype)
print(resim.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()