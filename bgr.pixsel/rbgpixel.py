import cv2
import numpy as np

space=cv2.imread("space.jpg")
cv2.imshow("space",space)
print(space[(230,80)])
print("Resmin Boyutu:  "  +str(space.size))
print("Resmin Özellikleri:  "  +str(space.shape))
print("Resmin Veri Tipi:  "  +str(space.dtype))


cv2.waitKey(0)
cv2.destroyAllWindows()



