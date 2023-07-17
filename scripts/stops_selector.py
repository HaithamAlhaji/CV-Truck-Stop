import cv2
import pickle

width, height = 100 - 70, 135 - 120

try:
    with open("./data/stops", "rb") as stops_file:
        lst_positions = pickle.load(stops_file)
except:
    lst_positions = []


def mouse_event_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        lst_positions.append((x, y))
        print(lst_positions[-1])
    elif event == cv2.EVENT_RBUTTONDOWN:
        for index, position in enumerate(lst_positions):
            if position[0] < x < position[0] + width and 4 < y < position[1] + height:
                print(f"Stop ({position[0]},{position[1]}) removed successfully.")
                lst_positions.pop(index)
            else:
                print("No stop found!")
    with open("./data/stops", "wb") as stops_file:
        pickle.dump(lst_positions, stops_file)


while True:
    img = cv2.imread("./footages/Footage 01.png")

    for position in lst_positions:
        cv2.rectangle(
            img=img,
            pt1=(position[0], position[1]),  # x,y
            pt2=(position[0] + width, position[1] + height),  # x,y
            color=(0, 255, 0),  # BGR
            thickness=1,
            lineType=cv2.LINE_4,
        )

    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouse_event_click)
    cv2.waitKey(1)
