# Gerekli paketleri içe aktarın!
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2


def convolve(image,kernel):
    # Görüntünün mekansal boyutları
    # Çekirdeğin mekansal boyutları
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # Çıktı görüntüsü için bellek ayırın, buna dikkat edin!
    # Giriş görüntüsünün sınırlarını doldurun!
    # Boyut (yani genişlik ve yükseklik) azaltılmaz!
    pad = (kW-1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
    cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32") 
    
    # Giriş görüntüsünün üzerinde döngü oluşturarak çekirdeği "kaydırır"
    # Her (x,y) koordinatı soldan sağa ve yukarıdan aşağıya
    # Alt
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # Görüntünün ROI'sini çıkarmak için
            # Geçerli (x,y) koordinatlarının merkez bölgesi
            # Boyutlar
            roi = image[y-pad:y + pad + 1, x - pad:x + pad + 1]

            # Gerçek evrişimi alarak gerçekleştirin!
            # ROI ile öğe bazında çarpın
            # Ve çekirdek, ardından matrisi topla!
            k = (roi * kernel) .sum()

            # Kıvrılmış değeri çıktıda (x,y) sakla
            # Çıktı görüntüsünün koordinatı
            output[y - pad, x - pad] = k
            # Çıktı görüntüsünü [0,255] aralığında olacak şekilde yeniden ölçeklendirin
            output = rescale_intensity(output, in_range=(0,255))
            output = (output * 255).astype("uint8")

            # Çıktı görüntüsüne yeniden dön.
            return output
 
 
        # Argümanı oluştur argümanları ayrıştır!
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True,
        help="path to input image")
        args = vars(ap.parse_args())

        # Bir görüntüyü yumuşatmak için kullanılan ortalama bulanıklaştırma çekirdekleri oluşturun
        smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
        largeBlur = np.ones((21, 21), dtype="float") * (1.0 /(21 * 21))

        # Bir şekillendirme filtresi inşa et!
        sharpen = np.array((
        [0, -1, 0],
        [-1, 5 ,-1],
        [0, -1, 0]), dtype="int")
         # Kenar benzerini algılamak için Laplace çekirdeğini oluşturun!
        # Bir görüntünün bölgeleri
        laplacian = np.array((
        [0, 1, 0],
        [1, -4, 1],
        [-1, 0, 1]), dtype="int")
        # Sobel x ekseni çekirdeğini oluştur
        sobelX = np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")
    
        # Sobel y çekirdeğini oluştur
        sobelY = np.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")
    
        # çekirdek bankasını, hem özel 'convolve' işlevimizi 
        # hem de OpenCV'nin 'filter2D' işlevini kullanarak
        # uygulayacağımız çekirdeklerin bir listesini oluşturun
        kernelBank = (
        ("small_blur", smallBlur),
        ("large_blur", largeBlur),
        ("sharpen", sharpen),
        ("laplacian", laplacian),
        ("sobel_x", sobelX),
        ("sobel_y", sobelY)
    )
    # Giriş resmini yükle ve gri ölçeğe dönüştür!
    image = cv2.imread(args["space.jpg"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # Kernel üzerinde döngüye al!
    for (kernelName, kernel) in kernelBank:
        # Çekirdeği hem özel 'convolve' fonksiyonumuz 
        # hem de openCV'nin 'filter2D' fonksiyonunu kullanarak
        # gri tonlamalı görüntüye uygulayın!  
        print("[INFO] applying {} kernel".format(kernelName))
        convolveOutput = convolve(gray, kernel)
        opencvOutput = cv2.filter2D(gray, -1, kernel)

        # Çıktı görüntüsünü göster!
        cv2.imshow("original", gray)
        cv2.imshow("{} - convolve".format(kernelName), convolveOutput)
        cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
        cv2.waitKey(0)
       

    cv2.destroyAllWindows()