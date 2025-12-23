import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg", 0)

kernel = cv2.getGaborKernel((21,21), 8.0, 0, 10.0, 0.5)
filtered = cv2.filter2D(img, cv2.CV_8UC3, kernel)

cv2.imshow("Original", img)
cv2.imshow("Gabor Filtered", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
