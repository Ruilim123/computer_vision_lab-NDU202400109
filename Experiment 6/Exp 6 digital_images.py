import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg")

# Averaging filter
kernel = np.ones((5,5), np.float32) / 25
filtered = cv2.filter2D(img, -1, kernel)

# Motion blur
motion_kernel = np.zeros((15,15))
motion_kernel[7, :] = 1 / 15
motion_blur = cv2.filter2D(img, -1, motion_kernel)

cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered)
cv2.imshow("Motion Blur", motion_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
