import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg", 0)

hist = cv2.calcHist([img], [0], None, [256], [0,256])
equalized = cv2.equalizeHist(img)

plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title("Original")
plt.subplot(2,2,2), plt.plot(hist)
plt.title("Histogram")
plt.subplot(2,2,3), plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")

plt.show()
