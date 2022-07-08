import cv2
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode=False, complexity=1, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # static_image_mode = False,
        # model_complexity = 1,
        # smooth_landmarks = True,
        # enable_segmentation = False,
        # smooth_segmentation = True,
        # min_detection_confidence = 0.5,
        # min_tracking_confidence = 0.5)

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.complexity, self.smooth, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        def findPose(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            result = self.pose.process(imgRGB)
            if draw:
            if result.pose_landmarks:
                self.mpDraw.draw_landmarks(img, result.pose_landmarks, self.mpPose.POSE_CONNECTIONS)


def rescale_frame(frame):
    # width = int(frame.shape[1] * percent / 100)
    # height = int(frame.shape[0] * percent / 100)
    width = 350
    height = 600
    dim = (width, height)
    return cv2.resize(frame, dim)

    # for id, lm in enumerate(result.pose_landmarks.landmark):
    #     h, w, c = img.shape
    #     print(id, lm)
    #     cx, cy = int(lm.x * w), int(lm.y * h)
    #     cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)


def main():
    cap = cv2.VideoCapture('production ID_4990426.mp4')
    pTime = 0

    # def change_res(width, height):
    #     cap.set(3, width)
    #     cap.set(4, height)

    while True:
        success, img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    # cv2.imshow("Image", img)
    img_rescale = rescale_frame(img)
    cv2.imshow('Image', img_rescale)
    cv2.waitKey(1)


if __name__ == "__main__":
    main()
