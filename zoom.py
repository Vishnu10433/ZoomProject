import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Load image
img1 = cv2.imread(r"D:\Users\Welcome\Desktop\ZoomProject\images\unnamed.webp")

if img1 is None:
    print("Failed to load image. Check file path.")
    exit()

# Original image size
orig_h, orig_w = img1.shape[:2]

# Limits for zoom
max_scale = 1.5
min_scale = 0.3

# Initial scale and center
scale = 0.5
cx, cy = 640, 360

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img, draw=False)

    if len(hands) == 2:
        # Get fingertips
        thumb1, index1 = hands[0]["lmList"][4], hands[0]["lmList"][8]
        thumb2, index2 = hands[1]["lmList"][4], hands[1]["lmList"][8]

        # Distance between thumb and index for each hand
        dist1 = np.linalg.norm(np.array(thumb1) - np.array(index1))
        dist2 = np.linalg.norm(np.array(thumb2) - np.array(index2))

        # Average distance -> scale factor
        avg_dist = (dist1 + dist2) / 2
        scale = np.clip(np.interp(avg_dist, [50, 250], [min_scale, max_scale]), min_scale, max_scale)

        # Center of zoom
        cx = int((thumb1[0] + index1[0] + thumb2[0] + index2[0]) / 4)
        cy = int((thumb1[1] + index1[1] + thumb2[1] + index2[1]) / 4)

        # Resize image
        newW, newH = int(orig_w * scale), int(orig_h * scale)
        resized_img = cv2.resize(img1, (newW, newH))

        # Calculate ROI on the camera frame
        top_left_x = max(0, cx - newW // 2)
        top_left_y = max(0, cy - newH // 2)
        bottom_right_x = min(img.shape[1], top_left_x + newW)
        bottom_right_y = min(img.shape[0], top_left_y + newH)

        # Crop resized image if it goes out of frame
        cropped_img = resized_img[0:bottom_right_y-top_left_y, 0:bottom_right_x-top_left_x]

        # Overlay image
        img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = cropped_img

    cv2.imshow("Hand Gesture Zoom", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
