
# Object Detection with YOLO and Flask

## Overview

This project implements an object detection system using the YOLO (You Only Look Once) model. The application allows users to upload images and receive real-time detection results, including bounding boxes around detected objects and corresponding JSON outputs.

## Output Image

![image1](https://github.com/user-attachments/assets/98957bf5-c71b-42d9-9732-4a01a41db6b0)

![image2](https://github.com/user-attachments/assets/ff5676e7-bacf-4893-935c-c7bfad2d6c90)

## JSON Format Output

![image](https://github.com/user-attachments/assets/833d7ec5-e0de-4379-b8d9-f8b45d979be6)


### Task Provided By

This project was developed as part of a task given by **AIMonk**.

## Features

- **Real-time Object Detection**: Leverage the YOLO model for efficient and accurate detection of multiple objects in images.
- **Web Interface**: A user-friendly interface built with Flask that allows image uploads and displays results.
- **JSON Output**: Detailed detection results are returned in JSON format, including object classes, confidence scores, and bounding box coordinates.

## Technologies Used

- **Python**: The primary programming language.
- **Flask**: A lightweight WSGI web application framework for Python.
- **Ultralytics YOLO**: A state-of-the-art object detection model for fast inference and high accuracy.
- **OpenCV**: For image processing and displaying results.
- **Docker**: For containerizing the application.

## Installation

### Prerequisites

- Python 3.9 or higher
- Docker (for containerization)

### Setup Instructions


## Install dependencies: Create a virtual environment (optional but recommended):  

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


## Install the required packages:

pip install -r requirements.txt

## Run the application:

python ui_service_main.py

Access the application in your browser at http://127.0.0.1:5000.

## Running with Docker

docker build -t aimonk-object-detection .

## Run the Docker container:

docker run -p 5000:5000 aimonk-object-detection

Access the application in your browser at http://127.0.0.1:5000.

## Output
## The application will generate:

A detected image with bounding boxes around the objects.
A JSON file containing details of the detected objects.




