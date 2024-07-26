# Hand Gesture Volume Control

This Python project uses hand gestures captured via a webcam to control the volume of your laptop. The project leverages OpenCV for image processing, MediaPipe for hand tracking, and Pycaw for volume control.

## Features

- Real-time hand tracking using a webcam.
- Control system volume by changing the distance between the thumb and index finger.
- Visual feedback showing the current volume level on the webcam feed.

## Installation

Before running the project, you need to install the required dependencies. Use pip to install them:

```sh
pip install opencv-python mediapipe pycaw
```

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

```sh
python volume_control.py
```

4. The webcam feed will open. Place your hand in front of the camera, and adjust the volume by moving your thumb and index finger closer or further apart.
5. Press 'q' to exit the application.

## Code Explanation

- **MediaPipe** is used for hand tracking, identifying the positions of the thumb and index finger.
- **PyCaw** controls the system volume based on the distance between the thumb and index finger.
- **OpenCV** handles the webcam feed and drawing of landmarks and feedback text on the screen.

## How It Works

1. The script initializes MediaPipe for hand tracking and PyCaw for volume control.
2. The webcam feed is processed frame by frame.
3. Hand landmarks are detected, and the positions of the thumb tip and index finger tip are identified.
4. The Euclidean distance between these two points is calculated.
5. This distance is mapped to the volume range of the system.
6. The system volume is adjusted accordingly, and the current volume level is displayed on the screen.

## Dependencies

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyCaw](https://github.com/AndreMiras/pycaw)

## Acknowledgements

- The [MediaPipe](https://mediapipe.dev/) library by Google for hand tracking.
- The [PyCaw](https://github.com/AndreMiras/pycaw) library for system volume control.

---
