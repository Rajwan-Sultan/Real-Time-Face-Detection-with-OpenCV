# 👁️ Real-Time Face Detection with OpenCV

This project uses OpenCV and a pre-trained Haar Cascade classifier to detect faces in real-time through your computer's webcam. Each detected face is highlighted with a colorful rectangle.

---

## 📸 Features

- 🧠 Uses Haar Cascade Classifier (`haarcascade_frontalface_default.xml`)
- 🎥 Real-time webcam face detection
- 🌈 Randomly colored rectangles for each detected face
- 🛑 Press `Q` or `q` to exit the webcam window

---

## 🚀 Quick Start

### 1️⃣ Prerequisites

- Python 3.x
- OpenCV
- Webcam

Install dependencies using pip:

```bash
pip install opencv-python
````

---

### 2️⃣ Setup

Download the Haar cascade file from OpenCV’s GitHub:

> [📥 Download XML File](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)

Place the file in the following path:

```
../trained_face_data/haarcascade_frontalface_default.xml
```

---

### 3️⃣ Run the Script

```bash
python face_detect.py
```

---

## 🧠 How It Works

1. Loads the Haar cascade XML file.
2. Captures video stream from the webcam.
3. Converts each frame to grayscale (since the classifier works better on grayscale).
4. Detects faces using the classifier.
5. Draws a randomly-colored rectangle around each detected face.
6. Press `Q` or `q` to exit.

---

## 📂 Project Structure

```
.
├── code/              
│   └── face.py                   # Main Python script
├── trained_face_data/
│   └── haarcascade_frontalface_default.xml
└── README.md                    # Project documentation
```

---

## 📌 Notes

* If detection is slow or unstable, try adjusting lighting or camera angle.
* The rectangle color is randomized for a fun, dynamic look.
* Make sure the XML file path is correct; otherwise, the classifier won’t load.

---

## 🛡️ License



Made  by **Rajwan Sultan**


