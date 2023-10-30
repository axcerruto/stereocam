#!/usr/bin/env python3
# Original Author: Antonio X Cerruto, 30-Oct-2023
from triangulator import Triangulator
from camera import Camera
from hands import HandDetector
import cv2

tr = Triangulator(120, 70.3)
cam_left = Camera(1)
cam_right = Camera(0)
detect_hands_left = HandDetector()
detect_hands_right = HandDetector()
while True:
	coords_left = None
	coords_right = None
	img_left = cam_left.get_frame()
	landmarks = detect_hands_left.get_landmarks(img_left)
	if(len(landmarks) > 0):
		coords_left = landmarks[0][8]

	img_right = cam_right.get_frame()
	landmarks = detect_hands_right.get_landmarks(img_right)
	if(len(landmarks) > 0):
		coords_right = landmarks[0][8]

	img = cv2.hconcat([img_left, img_right])
	cv2.imshow(f"[left, right] cameras", img)

	if(coords_left is not None and coords_right is not None):
		(x, y, z) = tr.pix2mm(coords_left, coords_right)
		print(f"{x}, {y}, {z}")

	if cv2.waitKey(5) == ord('q'):
		break
cam_left.close()
cam_right.close()
