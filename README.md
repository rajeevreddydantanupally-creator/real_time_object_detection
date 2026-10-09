# Real-Time Object Detection System

## Project Overview
This project detects people and common objects in real time
using a laptop webcam. It uses a pretrained YOLO deep-learning
model and OpenCV to display detection results.

## Features
- Real-time webcam object detection
- Detects people and supported everyday objects
- Displays bounding boxes, object labels, and confidence scores
- Press Q to exit the application

## Technologies Used
- Python
- Ultralytics YOLO
- OpenCV

## Installation

1. Install Python.
2. Clone or download this repository.
3. Create and activate a virtual environment.
4. Install the dependencies:

   pip install -r requirements.txt

## How to Run

Run this command from the project folder:

   python main.py

The pretrained YOLO model weights will download automatically
on the first run if they are not already available.

## How It Works
1. Capture a frame from the webcam.
2. Pass the frame to the pretrained YOLO model.
3. Detect supported objects and their locations.
4. Draw bounding boxes and labels.
5. Display the annotated frame.

## Machine Learning Approach
This project uses transfer learning through a pretrained
object detection model. It runs inference on live webcam
frames instead of training a new model from scratch.

## Limitations
Detection accuracy depends on lighting, camera quality,
object visibility, and the classes supported by the model.

## Author
Rajeev Reddy