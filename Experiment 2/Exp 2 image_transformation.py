import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg")
h, w = img.shape[:2]

# Scaling
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

# Translation
M = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(img, M, (w, h))

# Rotation
R = cv2.getRotationMatrix2D((w//2, h//2), 45, 1)
rotated = cv2.warpAffine(img, R, (w, h))

cv2.imshow("Original", img)
cv2.imshow("Scaled", scaled)
cv2.imshow("Translated", translated)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
