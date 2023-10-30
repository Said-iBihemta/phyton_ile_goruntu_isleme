import cv2
import numpy as np

resim=cv2.imread("Manzara.jpg")
cv2.imshow("Manzara",resim)

ayna=cv2.copyMakeBorder(resim,111,111,111,111,cv2.BORDER_REFLECT)
cv2.imshow("Ayna",ayna)
uzatma=cv2.copyMakeBorder(resim,133,133,153,153,cv2.BORDER_REPLICATE)
cv2.imshow("Uzatma",uzatma)
tekrarla=cv2.copyMakeBorder(resim,99,99,99,99,cv2.BORDER_WRAP)
cv2.imshow("Tekrarla",tekrarla)
sarma=cv2.copyMakeBorder(resim,33,33,33,33,cv2.BORDER_CONSTANT,value=(0,111,111))
cv2.imshow("Sarilan",sarma)

cv2.waitKey(0)
cv2.destroyAllWindows()
