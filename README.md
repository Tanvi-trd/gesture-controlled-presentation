Gesture Controlled Presentation System

This project is a Python-based computer vision application that allows users to control PowerPoint presentations using hand gestures captured through a webcam. It enables touchless slide navigation and zoom control without using a keyboard or mouse.

->>Features
- Real-time hand detection using webcam
- Next and previous slide navigation
- Zoom in and zoom out using gestures
- Works with PowerPoint slide show mode
- Simple and beginner-friendly implementation

->>Technologies Used
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

->>How It Works

The system captures live video from the webcam and detects hand landmarks using MediaPipe. Specific hand gestures are recognized based on finger count, and corresponding keyboard actions are triggered using PyAutoGUI to control the presentation.

->>Gesture Controls
- Two fingers: Next slide
- Three fingers: Previous slide
- Open palm (five fingers): Zoom in
- Fist (zero fingers): Zoom out

->> How to Run
1. Install Python 3.11 or above (MediaPipe supported version)
2. Install required libraries:
   pip install opencv-python mediapipe pyautogui numpy
3. Open PowerPoint and start slideshow (F5)
4. Run the program:
   python gesture_presentation.py
5. Show gestures in front of the webcam

->> Applications
- Touchless presentations
- Smart classrooms
- Assistive technology
- Interactive demonstrations

->> Future Enhancements
- Swipe-based gesture detection
- Voice feedback
- Support for PDF and video players
- Improved gesture accuracy

Author
Tanvi RD
