# coding=utf-8
import  cv2
import numpy as np
cap = cv2.VideoCapture(0)

first_threshold = 10
second_threshold=250

cv2.namedWindow("video")
cv2.namedWindow("canny")
cv2.namedWindow("blur")

while True:
    ret, frame = cap.read()  # Кадр за кадром
    framegrey1 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(framegrey1, (0,0), 2)
    edged = cv2.Canny(blur, first_threshold, second_threshold)
    circles =  cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, 2, 10, np.array([]), 40, 80, 5, 100)
    if circles is not None:
            for c in circles[0]:
                    cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0),2)
    edges = cv2.Canny( blur, 40, 80 )
    cv2.imshow("video", frame)
    cv2.imshow("edget", edges)
    #cv2.imshow("blur", blur)
    key = cv2.waitKey(30)