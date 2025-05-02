import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
import traceback

# Define the base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the target directories dynamically
target_dir = os.path.join(BASE_DIR, 'test_data_2.0', 'Gray_imgs', 'A')
count = len(os.listdir(target_dir))

p_dir = "A"
c_dir = "a"

offset = 30
step = 1
flag = False
suv = 0

# Initialize the white image for reference
white = np.ones((400, 400), np.uint8) * 255
output_path = os.path.join(BASE_DIR, 'white.jpg')
cv2.imwrite(output_path, white)

# Set up video capture
capture = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)

        img_final = img_final1 = img_final2 = 0

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            image = frame[y - offset:y + h + offset, x - offset:x + w + offset]

            roi = image     # RGB image without drawing

            # For grayscale image without draw
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (1, 1), 2)

            # For binary image
            gray2 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            blur2 = cv2.GaussianBlur(gray2, (5, 5), 2)
            th3 = cv2.adaptiveThreshold(blur2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            ret, test_image = cv2.threshold(th3, 27, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

            img_final1 = np.ones((400, 400), np.uint8) * 148
            h = test_image.shape[0]
            w = test_image.shape[1]
            img_final1[((400 - h) // 2):((400 - h) // 2) + h, ((400 - w) // 2):((400 - w) // 2) + w] = test_image

            img_final = np.ones((400, 400), np.uint8) * 255
            h = test_image.shape[0]
            w = test_image.shape[1]
            img_final[((400 - h) // 2):((400 - h) // 2) + h, ((400 - w) // 2):((400 - w) // 2) + w] = test_image

        hands = hd.findHands(frame, draw=False, flipType=True)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            image = frame[y - offset:y + h + offset, x - offset:x + w + offset]
            image_path = os.path.join(BASE_DIR, 'white.jpg')
            white = cv2.imread(image_path)

            handz = hd2.findHands(image, draw=False, flipType=True)
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

                for i in range(21):
                    cv2.circle(white, (pts[i][0] + os, pts[i][1] + os1), 2, (0, 0, 255), 1)

                cv2.imshow("skeleton", white)

            hands = hd.findHands(white, draw=False, flipType=True)
            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']
                cv2.rectangle(white, (x - offset, y - offset), (x + w, y + h), (3, 255, 25), 3)

            image1 = frame[y - offset:y + h + offset, x - offset:x + w + offset]
            roi1 = image1  # RGB image with drawing

            gray1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
            blur1 = cv2.GaussianBlur(gray1, (1, 1), 2)

            test_image2 = blur1
            img_final2 = np.ones((400, 400), np.uint8) * 148
            h = test_image2.shape[0]
            w = test_image2.shape[1]
            img_final2[((400 - h) // 2):((400 - h) // 2) + h, ((400 - w) // 2):((400 - w) // 2) + w] = test_image2

            cv2.imshow("binary", img_final)
            cv2.imshow("gray w/o draw", img_final1)

        # Collect and save data
        interrupt = cv2.waitKey(1)
        if interrupt & 0xFF == 27:
            break

        if interrupt & 0xFF == ord('n'):
            p_dir = chr(ord(p_dir) + 1)
            c_dir = chr(ord(c_dir) + 1)
            if ord(p_dir) == ord('Z') + 1:
                p_dir = "A"
                c_dir = "a"
            flag = False
            count = len(os.listdir(os.path.join(BASE_DIR, 'test_data_2.0', 'Gray_imgs', p_dir)))

        if interrupt & 0xFF == ord('a'):
            flag = not flag

        if flag:
            if suv == 50:
                flag = False
            if step % 2 == 0:
                # Save test data
                test_img_path = os.path.join(BASE_DIR, 'test_data_2.0', 'Gray_imgs', p_dir, f"{c_dir}{count}.jpg")
                cv2.imwrite(test_img_path, img_final1)

                test_img_path_with_drawing = os.path.join(BASE_DIR, 'test_data_2.0', 'Gray_imgs_with_drawing', p_dir, f"{c_dir}{count}.jpg")
                cv2.imwrite(test_img_path_with_drawing, img_final2)

                count += 1
                suv += 1
            step += 1

    except Exception:
        print("==", traceback.format_exc())

capture.release()
cv2.destroyAllWindows()
