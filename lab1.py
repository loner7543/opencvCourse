import cv2
image = cv2.imread("image/ball.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("image/grayBall.jpg", gray)