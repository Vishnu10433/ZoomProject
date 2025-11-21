# Hand-Gesture Zoom Project

This project is a **computer vision application** that allows you to **zoom in and out of an image using hand gestures** via your webcam. It is built using **Python 3.11**, **OpenCV**, **Mediapipe**, and **CVZone**.

---

## Features

- **Zoom with hand gestures**: Move your hands apart to zoom in, bring them closer to zoom out.
- **Real-time webcam interaction**: The program processes the camera feed live.
- **Multiple image support**: Place any image in the `images/` folder and control its zoom.
- **Cross-platform friendly**: Works on Windows with Python 3.11.
- **Lightweight**: Uses Mediapipe’s hand detection for fast performance.

---

## How It Works

1. The program captures the webcam feed using OpenCV.
2. Mediapipe’s **HandDetector** identifies hands and key landmarks (thumb and index finger tips).
3. The distance between the fingers is calculated to determine zoom scale.
4. The image is resized according to this scale and displayed on the live webcam feed.
5. The user can interact with the image in **real time** without touching the mouse or keyboard.

---

## Project Structure

