# DrowsyXNet – Real-Time Accident Prevention System Using Machine Learning

## Overview

DrowsyXNet is an AI-powered real-time driver monitoring and accident prevention system designed to improve road safety by detecting driver drowsiness, fatigue, yawning, eye closure, and mobile phone usage while driving. The system uses Deep Learning and Computer Vision techniques to continuously monitor driver behavior through a live webcam feed and provide instant alerts whenever unsafe driving conditions are detected.

The project aims to reduce accidents caused by driver distraction and fatigue by providing early warnings before critical situations occur.

---

## Features

* Real-time driver monitoring using webcam
* Drowsiness detection
* Eye closure detection
* Yawning detection
* Fatigue analysis
* Mobile phone usage detection
* Instant warning alerts
* Live video streaming
* Deep Learning based prediction system
* User-friendly web interface
* Real-time accident prevention support

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Django

### Machine Learning & AI

* TensorFlow
* Keras
* OpenCV
* CNN (Convolutional Neural Network)
* ResNet Architecture

### Other Tools

* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## System Architecture

1. Webcam captures live video feed.
2. Video frames are processed using OpenCV.
3. Frames are passed to trained Deep Learning models.
4. The model predicts:

   * Eye state
   * Yawning
   * Fatigue
   * Mobile phone usage
5. If abnormal behavior is detected:

   * Warning alert is triggered
   * Driver is notified immediately

---

## Working of the System

### 1. Data Collection

Datasets containing driver images/videos were collected for:

* Open eyes
* Closed eyes
* Yawning
* Fatigue detection
* Mobile phone usage

### 2. Data Preprocessing

* Image resizing
* Normalization
* Frame extraction
* Data augmentation

### 3. Model Training

CNN and ResNet models were trained using TensorFlow/Keras for accurate real-time predictions.

### 4. Real-Time Detection

The trained model processes live video frames continuously and identifies dangerous driver behavior instantly.

### 5. Alert Generation

Whenever drowsiness or distraction is detected for a specific duration, the system generates:

* Audio alert
* Visual warning

---

## Project Modules

### Driver Monitoring Module

Tracks driver facial movements and eye activity.

### Drowsiness Detection Module

Detects prolonged eye closure and fatigue patterns.

### Yawning Detection Module

Identifies continuous yawning behavior.

### Mobile Usage Detection Module

Detects whether the driver is using a mobile phone while driving.

### Alert System

Provides instant warning notifications.

---

## Folder Structure

```bash
DrowsyXNet/
│
├── static/
├── templates/
├── model/
├── dataset/
├── app.py
├── predict.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/DrowsyXNet.git
```

### Navigate to Project Directory

```bash
cd DrowsyXNet
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

---

## Future Enhancements

* Integration with IoT devices
* GPS-based emergency alerts
* Cloud-based monitoring system
* Advanced driver analytics
* Night vision support
* Multi-driver recognition system

---

## Advantages

* Helps reduce road accidents
* Real-time monitoring
* Fast and accurate predictions
* Low-cost safety solution
* Easy to deploy

---

## Applications

* Smart vehicles
* Driver safety systems
* Fleet management
* Transportation industry
* Public transport monitoring

---

## Conclusion

DrowsyXNet is an intelligent real-time accident prevention system that combines Machine Learning, Deep Learning, and Computer Vision to improve driver safety. By continuously monitoring driver behavior and generating instant alerts, the system helps prevent accidents caused by drowsiness and distraction.

---

## Authors

* Swetha Saju


---

## License

This project is developed for educational and research purposes.
