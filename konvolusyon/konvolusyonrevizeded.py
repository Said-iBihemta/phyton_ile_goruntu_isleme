# Gerekli paketleri içe aktarın!
from skimage.exposure import rescale_intensity
import numpy as np
import cv2


def conolve(image, kernel):
    # Görüntünün mekansal boyutları
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # Giriş görüntüsünün sınırlarını doldurun!
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    
    # Çıktı görüntüsü için bellek ayırın
    output = np.zeros((iH, iW), dtype="float32")

    # Kernel kaydırma işlemi
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # Görüntünün ROI (Region of Interest) bölgesi
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            # Konvolüsyon işlemi
            k = (roi * kernel).sum()
            output[y - pad, x - pad] = k

    # Çıktıyı [0,255] aralığında yeniden ölçeklendir
    output = rescale_intensity(output, in_range=(output.min(), output.max()))
    output = (output * 255).astype("uint8")

    return output


# Giriş resmini yükle ve gri ölçeğe dönüştür!
image = cv2.imread("space.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Farklı çekirdek filtreleri oluştur
smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

# Kernel listesini oluştur
kernelBank = [
    ("small_blur", smallBlur),
    ("large_blur", largeBlur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobelX),
    ("sobel_y", sobelY)
]

# Kernel üzerinde döngü
for (kernelName, kernel) in kernelBank:
    print("[INFO] applying {} kernel".format(kernelName))
    conolveOutput = conolve(gray, kernel)
    opencvOutput = cv2.filter2D(gray, -1, kernel)

    # Çıktı görüntüsünü göster
    cv2.imshow("Original", gray)
    cv2.imshow("{} - conolve".format(kernelName), conolveOutput)
    cv2.imshow("{} - OpenCV".format(kernelName), opencvOutput)
    cv2.waitKey(0)

cv2.destroyAllWindows()
