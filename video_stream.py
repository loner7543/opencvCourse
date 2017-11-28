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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("image/grayBall.jpg", gray)
    edged = cv2.Canny(gray, first_threshold,
                      second_threshold)  # find borders use canny-algoritm на вход подаются 2 пороговых значения
    cv2.imwrite("image/borders.jpg", edged)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, acc, 2,
                               100)  # save resolution, 100 - Minimum distance between the centers of the detected circles Hough transform1-same resolution
    if circles is not None:# Если нашли окружности по Хафу
        print ("------------Найдена окружность---------")
        circles = np.round(circles[0, :]).astype("int")  # double to int
        for (x, y, r) in circles:  # loop over the (x, y) coordinates and radius of the circles
            cv2.circle(image, (x, y), r, (0, 255, 0), border_size)
            # print(x)
            # print (y)
            cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), center_color, -1)
    else:print ("Не найдено")
print (cv2.__version__)
cap = cv2.VideoCapture(default_camera)




while(True):
    ret,frame = cap.read()# Кадр за кадром
    findCenter(frame)
    #cv2.imwrite("image/frame.jpg", frame)
    cv2.imshow('frame', frame)# окно с кадрами

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()