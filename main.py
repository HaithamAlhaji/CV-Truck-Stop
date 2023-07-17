import cv2
import numpy as np
import pickle

width, height = 100 - 70, 135 - 120

try:
    with open("./data/stops", "rb") as stops_file:
        print("dddd")
        lst_positions = pickle.load(stops_file)
except:
    lst_positions = []

cap = cv2.VideoCapture("./footages/Footage 01.mp4")


def stops_checker(imgProc):
    numberOfFreeStops = 0
    for position in lst_positions:
        pass
        imgCropped = imgProc[
            position[1] : position[1] + height, position[0] : position[0] + width
        ]
        # cv2.imshow(str(position[0] * position[1]), imgCropped)
        numberOfPixels = cv2.countNonZero(imgCropped)

        # # Print numberOfPixel above rectangle
        # cv2.putText(
        #     img,
        #     str(numberOfPixels),
        #     position,
        #     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        #     fontScale=0.4,
        #     color=(0, 255, 0),
        # )
        if numberOfPixels < 100:
            rectangleColor = (0, 255, 0)
            numberOfFreeStops += 1
        else:
            rectangleColor = (0, 0, 255)
            numberOfFreeStops -= 1

        cv2.rectangle(
            img=img,
            pt1=(position[0], position[1]),  # x,y
            pt2=(position[0] + width, position[1] + height),  # x,y
            color=rectangleColor,  # BGR
            thickness=1,
            lineType=cv2.LINE_4,
        )

    # TODO: enhance number of pixel for each car
    # cv2.putText(
    #     img,
    #     f"{numberOfFreeStops} of {len(lst_positions)}",
    #     (10, 30),
    #     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    #     fontScale=0.8,
    #     color=(0, 255, 0),
    # )


while True:
    # replay video again
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    # cvt image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 5)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 17
    )
    imgMedium = cv2.medianBlur(imgThreshold, 5)

    # TODO: needs more enhancement
    imgDilate = cv2.dilate(imgMedium, kernel=np.ones((3, 3), np.uint8), iterations=1)
    stops_checker(imgDilate)

    cv2.imshow("image", img)
    # # B/W image to check pixels
    # cv2.imshow("imgDilate", imgDilate)
    cv2.waitKey(10)
