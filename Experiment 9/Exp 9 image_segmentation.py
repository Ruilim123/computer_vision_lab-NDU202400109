import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Original", img)
cv2.imshow("Segmented", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
