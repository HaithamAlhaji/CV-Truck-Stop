import cv2
import pickle

# Set the dimensions of the region of interest for stops
width, height = 100 - 70, 135 - 120

# Load previously saved stop positions from a pickle file if available, otherwise start with an empty list
try:
    with open("./data/stops", "rb") as stops_file:
        lst_positions = pickle.load(stops_file)
except:
    lst_positions = []


# Define a function to handle mouse events (clicks) on the image
def mouse_event_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # If the left mouse button is clicked, add the clicked position to the list of stops
        lst_positions.append((x, y))
        print(lst_positions[-1])
    elif event == cv2.EVENT_RBUTTONDOWN:
        # If the right mouse button is clicked, check if there is a stop at the clicked position and remove it if found
        for index, position in enumerate(lst_positions):
            if position[0] < x < position[0] + width and 4 < y < position[1] + height:
                print(f"Stop ({position[0]},{position[1]}) removed successfully.")
                lst_positions.pop(index)
            else:
                print("No stop found!")

    # Save the updated list of stops to the pickle file
    with open("./data/stops", "wb") as stops_file:
        pickle.dump(lst_positions, stops_file)


while True:
    # Read the image from file
    img = cv2.imread("./footages/Footage 01.png")

    # Draw rectangles around the stops on the image
    for position in lst_positions:
        cv2.rectangle(
            img=img,
            pt1=(position[0], position[1]),  # x, y of the top-left corner
            pt2=(
                position[0] + width,
                position[1] + height,
            ),  # x, y of the bottom-right corner
            color=(0, 255, 0),  # BGR color of the rectangle (green)
            thickness=1,
            lineType=cv2.LINE_4,
        )

    # Display the image with the rectangles indicating the stops
    cv2.imshow("image", img)

    # Set the mouse callback function to handle mouse events on the image
    cv2.setMouseCallback("image", mouse_event_click)

    # Wait for 1 millisecond for a key press
    cv2.waitKey(1)
