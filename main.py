import cv2
import numpy as np
import pickle

# Set the dimensions of the region of interest for stops checking
width, height = 100 - 70, 135 - 120

# Load previously saved stop positions from a pickle file if available, otherwise start with an empty list
try:
    with open("./data/stops", "rb") as stops_file:
        print("dddd")
        lst_positions = pickle.load(stops_file)
except:
    lst_positions = []

# Open the video file for processing
cap = cv2.VideoCapture("./footages/Footage 01.mp4")


# Define a function to check for stops in the processed image
def stops_checker(imgProc):
    numberOfFreeStops = 0
    for position in lst_positions:
        # Crop the region of interest from the processed image
        imgCropped = imgProc[
            position[1] : position[1] + height, position[0] : position[0] + width
        ]

        # Calculate the number of non-zero pixels in the cropped image (non-black pixels)
        numberOfPixels = cv2.countNonZero(imgCropped)

        # Determine whether the stop region has enough free space based on the number of pixels
        # If the number of pixels is less than 100, consider it as a free stop, otherwise it's occupied
        if numberOfPixels < 100:
            rectangleColor = (0, 255, 0)  # Green color for free stop
            numberOfFreeStops += 1
        else:
            rectangleColor = (0, 0, 255)  # Red color for occupied stop
            numberOfFreeStops -= 1

        # Draw a rectangle around the stop region on the original image
        cv2.rectangle(
            img=img,
            pt1=(position[0], position[1]),  # x, y of the top-left corner
            pt2=(
                position[0] + width,
                position[1] + height,
            ),  # x, y of the bottom-right corner
            color=rectangleColor,  # BGR color of the rectangle
            thickness=1,
            lineType=cv2.LINE_4,
        )

    # TODO: Enhance the number of pixels for each car before displaying it
    # cv2.putText(
    #     img,
    #     f"{numberOfFreeStops} of {len(lst_positions)}",
    #     (10, 30),
    #     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    #     fontScale=0.8,
    #     color=(0, 255, 0),
    # )


while True:
    # Replay the video when it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read a frame from the video stream
    success, img = cap.read()

    # Convert the image to grayscale and apply some image processing techniques
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 5)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 17
    )
    imgMedium = cv2.medianBlur(imgThreshold, 5)

    # TODO: More enhancements required
    # Perform dilation to connect and enhance the areas of interest (stops)
    imgDilate = cv2.dilate(imgMedium, kernel=np.ones((3, 3), np.uint8), iterations=1)

    # Call the stops_checker function to check for stops and draw rectangles on the image
    stops_checker(imgDilate)

    # Display the original image with the rectangles indicating the stops
    cv2.imshow("image", img)

    # Wait for 10 milliseconds and check for any key press
    cv2.waitKey(10)
