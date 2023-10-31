import cv2
import numpy as np

resim1=cv2.imread("1.jpg")
resim2=cv2.imread("2.jpg")

print(resim1[100,200])
print(resim2[333,444])

cv2.imshow("uretim",resim1)
cv2.imshow("Kuru Kafa",resim2)

print(resim1[100,200]+resim2)


cv2.waitKey(0)
cv2.destroyAllWindows()