import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg")

# Smoothing
blur = cv2.GaussianBlur(img, (5,5), 0)

# Sharpening
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
