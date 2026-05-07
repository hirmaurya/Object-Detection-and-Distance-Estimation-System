# Object-Detection-and-Distance-Estimation-System

# VisionAssist: Real-Time Object Detection for Navigation

VisionAssist is a Python-based computer vision project designed to help users identify and navigate around objects in real-time. By leveraging the **YOLOv8** (You Only Look Once) model, the system detects objects via a camera feed and provides feedback on the object's name, horizontal direction (Left, Center, Right), and estimated distance.

## 🚀 Features
* **Real-Time Detection:** Uses `yolov8n.pt` (Nano) for high-speed performance.
* **Spatial Awareness:** Calculates whether an object is to the left, right, or center of the frame.
* **Distance Estimation:** Categorizes proximity (1m, 2m, or 3+ meters) based on the bounding box width relative to the frame size.
* **Dual Camera Support:** Configured to work with external camera sources (e.g., iPhone via Continuity Camera or USB webcams).

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** * `OpenCV`: For video capturing and image processing.
    * `Ultralytics YOLOv8`: For state-of-the-art object detection.
    * `PyTorch`: Backend for model inference.

## 📁 File Structure
* `blind_assist.py`: The main application script for detection and spatial logic.
* `yolo_test.py`: A utility script to verify YOLO installation and model loading.
* `camera_test.py`: A diagnostic tool to ensure the camera index (e.g., `cv2.VideoCapture(1)`) is correctly identified.
* `yolov8n.pt`: The pre-trained weights for the YOLOv8 Nano model.

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/VisionAssist.git
    cd VisionAssist
    ```

2.  **Install dependencies:**
    ```bash
    pip install ultralytics opencv-python torch
    ```

3.  **Run the application:**
    First, ensure your camera is connected, then run:
    ```bash
    python blind_assist.py
    ```

## 📊 Logic Overview
The system splits the video frame into three vertical sectors:
* **Left:** Center of object is in the first 33% of the width.
* **Center:** Center of object is between 33% and 66%.
* **Right:** Center of object is in the last 33%.

Distance is estimated by the percentage of the frame the object occupies:
* **> 40% width:** ~1 meter away.
* **> 20% width:** ~2 meters away.
* **Otherwise:** 3+ meters away.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### A few tips for your GitHub:
1.  **Add a .gitignore:** Since `yolov8n.pt` is a large binary file, it's often better to let the script download it automatically rather than pushing it to Git. If you want to keep the repo clean, add `*.pt` to your `.gitignore`.
2.  **Requirements.txt:** You can generate a requirements file by running `pip freeze > requirements.txt` so others can install dependencies easily.
3.  **Demo:** If you can, record a short GIF of the detection working and add it to the README to make it pop!
