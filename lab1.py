import numpy as np
import cv2
acc=1#storage space
first_threshold = 10
second_threshold=250
border_size=2
center_color=(0, 128, 255)

image = cv2.imread("image/ball.jpg")
output = image.copy()
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
cv2.imwrite("image/grayBall.jpg", gray)
edged = cv2.Canny(gray, first_threshold, second_threshold)# find borders use canny-algoritm
cv2.imwrite("image/borders.jpg",edged)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,acc,2,100)# save resolution, 100 - Minimum distance between the centers of the detected circles Hough transform1-same resolution
if circles is not None:
 circles = np.round(circles[0, :]).astype("int")# convert the (x, y) coordinates and radius of the circles to integers
 for (x, y, r) in circles: # loop over the (x, y) coordinates and radius of the circles
  # draw the circle in the output image, then draw a rectangle
  # corresponding to the center of the circle
  cv2.circle(output, (x, y), r, (0, 255, 0), border_size)
  cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), center_color, -1)

 cv2.imshow("output", np.hstack([image, output]))
 cv2.waitKey(0)