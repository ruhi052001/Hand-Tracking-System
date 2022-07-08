import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('production ID_4990426.mp4')
pTime = 0

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame):
    # width = int(frame.shape[1] * percent / 100)
    # height = int(frame.shape[0] * percent / 100)
    width = 350
    height = 600
    dim = (width, height)
    return cv2.resize(frame, dim)


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    # print(result.pose_landmarks)
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    # cv2.imshow("Image", img)
    img_rescale = rescale_frame(img)
    cv2.imshow('Image', img_rescale)
    cv2.waitKey(1)

