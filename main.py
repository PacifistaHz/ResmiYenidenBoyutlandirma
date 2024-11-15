import cv2

# Görüntü dosyasının yolu
yol = "scream.jpg"

# Görüntüyü oku
resim = cv2.imread(yol)

# Kalite değeri belirle
kaliteDegeri = 100

# Görüntüyü yeni bir dosya olarak kaydet ve kalite ayarlarını uygula
cv2.imwrite("scream_high_quality.jpg", resim, [int(cv2.IMWRITE_JPEG_QUALITY), kaliteDegeri])
