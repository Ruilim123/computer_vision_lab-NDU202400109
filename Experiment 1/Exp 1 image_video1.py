import cv2

# Image reading
img = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg", cv2.IMREAD_COLOR)
gray = cv2.imread(r"C:\Users\Ruilim\Desktop\CV\puppy CV.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Color Image", img)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Live video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Live Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
