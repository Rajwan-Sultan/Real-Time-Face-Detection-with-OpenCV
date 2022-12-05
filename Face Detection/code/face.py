import cv2
from random import randrange

""" https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml """


ai_path = '../trained_face_data/haarcascade_frontalface_default.xml'


trained_face_data = cv2.CascadeClassifier(ai_path)

webcam = cv2.VideoCapture(0)


while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    for x, y, w, h in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      (randrange(186, 255), randrange(186, 255), randrange(186, 255)), 5)
    cv2.imshow("Sultan", frame)
    key = cv2.waitKey(1)  # 1 mili_seconds
    # Stop if "Q/q" is pressed
    if key == 81 or key == 113:
        webcam.release()
        break

print("Completed")
