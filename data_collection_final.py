import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
import traceback

capture = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

# Get the base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directory where 'Gray_imgs' and 'A' are located (relative path)
target_dir = os.path.join(BASE_DIR, 'test_data_2.0', 'Gray_imgs', 'A')
count = len(os.listdir(target_dir))
c_dir = 'A'

offset = 15
step = 1
flag = False
suv = 0

# Create a white image
white = np.ones((400, 400), np.uint8) * 255
# Save white image in the same directory
output_path = os.path.join(BASE_DIR, 'white.jpg')
cv2.imwrite(output_path, white)

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)

        # Update white image path (relative to script location)
        image_path = os.path.join(BASE_DIR, 'white.jpg')
        white = cv2.imread(image_path)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            image = np.array(frame[y - offset:y + h + offset, x - offset:x + w + offset])

            handz, imz = hd2.findHands(image, draw=True, flipType=True)
            if handz:
                hand = handz[0]
                pts = hand['lmList']

                os = ((400 - w) // 2) - 15
                os1 = ((400 - h) // 2) - 15
                for t in range(0, 4, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                             (0, 255, 0), 3)
                for t in range(5, 8, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                             (0, 255, 0), 3)
                for t in range(9, 12, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                             (0, 255, 0), 3)
                for t in range(13, 16, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                             (0, 255, 0), 3)
                for t in range(17, 20, 1):
                    cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                             (0, 255, 0), 3)
                cv2.line(white, (pts[5][0] + os, pts[5][1] + os1), (pts[9][0] + os, pts[9][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[9][0] + os, pts[9][1] + os1), (pts[13][0] + os, pts[13][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[13][0] + os, pts[13][1] + os1), (pts[17][0] + os, pts[17][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os, pts[0][1] + os1), (pts[5][0] + os, pts[5][1] + os1), (0, 255, 0), 3)
                cv2.line(white, (pts[0][0] + os, pts[0][1] + os1), (pts[17][0] + os, pts[17][1] + os1), (0, 255, 0), 3)

                skeleton0 = np.array(white)
                zz = np.array(white)
                for i in range(21):
                    cv2.circle(white, (pts[i][0] + os, pts[i][1] + os1), 2, (0, 0, 255), 1)

                skeleton1 = np.array(white)

                cv2.imshow("1", skeleton1)

        frame = cv2.putText(frame, "dir=" + str(c_dir) + "  count=" + str(count), (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        interrupt = cv2.waitKey(1)
        if interrupt & 0xFF == 27:
            break  # esc key

        if interrupt & 0xFF == ord('n'):
            c_dir = chr(ord(c_dir) + 1)
            if ord(c_dir) == ord('Z') + 1:
                c_dir = 'A'
            flag = False
            target_dir = os.path.join(BASE_DIR, 'sign2text_dataset_3.0', 'AtoZ_3.0', c_dir)
            count = len(os.listdir(target_dir))
        if interrupt & 0xFF == ord('a'):
            flag = not flag
            suv = 0 if flag else suv

        if flag:
            if suv == 180:
                flag = False
            if step % 3 == 0:
                output_dir = os.path.join(BASE_DIR, 'sign2text_dataset_3.0', 'AtoZ_3.1', c_dir)

                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, f'{str(count)}.jpg')
                cv2.imwrite(output_path, skeleton1)

                count += 1
                suv += 1
            step += 1

    except Exception:
        print("==", traceback.format_exc())

capture.release()
cv2.destroyAllWindows()
