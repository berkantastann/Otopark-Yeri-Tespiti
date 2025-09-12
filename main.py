import cv2 as cv
from util import get_parking_spots_bboxes, empty_or_not
import numpy as np

def calc_diff(img1, img2):
    return np.abs(np.mean(img1) - np.mean(img2))

mask_path = "/Users/berkantastan/Documents/GitHub/Otopark-Yeri-Tespiti/mask_1920_1080.png"
video_path = "data/parking_1920_1080_loop.mp4"

mask = cv.imread(mask_path, cv.IMREAD_GRAYSCALE)
cap = cv.VideoCapture(video_path)

connected_components = cv.connectedComponentsWithStats(mask, 4, cv.CV_32S)
spots = get_parking_spots_bboxes(connected_components)

spots_status = [None for _ in spots]
diffs = [0 for _ in spots]

previous_frame = None
frame_number = 0
ret = True
step = 30

while ret:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_number % step == 0 and previous_frame is not None:
        for spot_idx, spot in enumerate(spots):
            x, y, w, h = spot
            spot_crop = frame[y:y + h, x:x + w]
            prev_crop = previous_frame[y:y + h, x:x + w]

            diffs[spot_idx] = calc_diff(spot_crop, prev_crop)

    if frame_number % step == 0:
        if previous_frame is None:
            arr_ = range(len(spots))
        else:
            # Büyük farkı olan spotları seç
            arr_ = [j for j in np.argsort(diffs) if diffs[j] / np.amax(diffs) > 0.4]

        # Seçilen spotlarda boş/dolu kontrolü yap
        for spot_idx in arr_:
            x, y, w, h = spots[spot_idx]
            spot_crop = frame[y:y + h, x:x + w]
            spot_status = empty_or_not(spot_crop)
            spots_status[spot_idx] = spot_status

    if frame_number % step == 0:
        previous_frame = frame.copy()

    # Çizim
    for spot_idx, spot in enumerate(spots):
        x, y, w, h = spots[spot_idx]
        spot_status = spots_status[spot_idx]

        if spot_status:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.putText(frame,"Available spots: {} / {}".format(str(sum(spots_status)), str(len(spots_status))) , (100,60), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv.namedWindow("frame", cv.WINDOW_NORMAL)
    cv.imshow("frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1

cap.release()
cv.destroyAllWindows()