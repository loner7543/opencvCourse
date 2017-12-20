# coding=utf-8
import cv2
import numpy as np

acc=1#storage space
first_threshold = 10
second_threshold=250
border_size=2
center_color=(0, 128, 255)

any_camera=-1
default_camera=-1
sleep=60# задержка кадра каждую минуту
fps=16

def findCenter(image):# по кадрам находит шар в видеопотоке
    noBlur = cv2.medianBlur(frame,3,frame)
    hsv_image = cv2.cvtColor(noBlur, cv2.COLOR_BGR2HSV)
    lower_red_hue_range=cv2.inRange(hsv_image, np.array([0, 100, 100]), np.array([0, 255, 255]))
    upper_red_hue_range=cv2.inRange(hsv_image, np.array([160, 100, 100]),np.array([179, 255, 255]))
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)
    cv2.imshow('images/combine.jpg', red_hue_image)
    #noBlur = cv2.GaussianBlur(red_hue_image, red_hue_image,(9, 9), 2, 2)
    conturs = cv2.Canny(red_hue_image, first_threshold, second_threshold)
    # cv2.imshow('images/conturs.jpg', conturs)
    #circles = cv2.HoughCircles(red_hue_image, cv2.HOUGH_GRADIENT, acc, 2)
    circles=cv2.HoughCircles(red_hue_image, cv2.HOUGH_GRADIENT, 1, 100)
    if circles is not None:# Если нашли окружности по Хафу
        print ("------------Найдена окружность---------")
        circles = np.round(circles[0, :]).astype("int")  # double to int
        for (x, y, r) in circles:  # loop over the (x, y) coordinates and radius of the circles
            cv2.circle(image, (x, y), r, (0, 255, 0), border_size)
            cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), center_color, -1)
    else:print ("Не найдено")
print (cv2.__version__)
cap = cv2.VideoCapture(default_camera)

while(True):
    ret,frame = cap.read()# Кадр за кадром
    findCenter(frame)
    cv2.imshow('frame', frame)# окно с кадрами

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()