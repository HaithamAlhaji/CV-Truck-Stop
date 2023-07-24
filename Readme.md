![](https://github.com/HaithamAlhaji/CV-Truck-Stop/blob/main/footages/result.gif)

# Stops Checker

This Python script processes a video file to detect and track stops. It identifies regions of interest that potentially represent stops and determines whether they are occupied or free.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Pickle (`pickle`)

You can install these libraries using the following command:

pip install opencv-python numpy

## How it works

1. The script loads the previously saved stop positions from a pickle file. If the file is not found or contains no data, it initializes an empty list to start tracking stop positions.

2. It opens a video file for processing. The path of the video file is provided in the code (`"./footages/Footage 01.mp4"`). Make sure to update the path if using a different video.

3. The `stops_checker` function is defined, which takes the processed image as input. The function iterates through the list of stop positions and checks each region of interest for occupancy.

4. For each position, the script crops the region of interest from the processed image and calculates the number of non-zero pixels (non-black pixels). If the number of pixels is below a threshold value (100 in this case), the stop is considered free; otherwise, it is considered occupied.

5. A rectangle is drawn around each stop region on the original image to indicate its status (green for free and red for occupied).

6. The script continuously reads frames from the video stream, processes them, and displays the original image with the rectangles indicating the stops and their occupancy status.

7. To replay the video when it reaches the end, the script sets the frame position back to 0.

## Usage

1. Make sure you have the required libraries installed as mentioned in the **Prerequisites** section.

2. Ensure you have a video file of traffic footage that you want to analyze for stops. Update the `cap = cv2.VideoCapture("./footages/Footage 01.mp4")` line with the correct path to your video file.

3. Run the Python script, and it will process the video and display the results.

4. The script will continuously display the processed frames with rectangles indicating the stops and their occupancy status. Press any key to stop the video playback and close the window.

5. To replay the video, the script will automatically restart when it reaches the end.

## Note

- The script currently performs basic image processing techniques to detect stops. Depending on the characteristics of the input video, you may need to fine-tune the parameters and add more advanced image processing techniques to achieve better results.

- The script contains commented-out code (`TODO` sections) that indicates areas for further enhancements. Feel free to uncomment and modify these sections to improve the script's functionality and visualization.

- If you want to save the detected stop positions for future use, you can modify the script to save the updated `lst_positions` list to a pickle file at the end of the processing.

- Make sure to have sufficient computing resources to run the script for longer videos, as video processing can be computationally intensive.

---

**Disclaimer:** This script is provided for educational and demonstrative purposes only. The performance of the stop detection algorithm heavily depends on the characteristics of the input video and the quality of the stops' representation. It may not be suitable for all scenarios and may require further optimization and refinement for real-world applications. Use it at your own risk.
