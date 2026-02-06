import cv2
import mediapipe as mp
import pyautogui
import time

# Webcam
cap = cv2.VideoCapture(0)

# MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Finger tip landmarks
fingerTips = [4, 8, 12, 16, 20]

# Delay to avoid repeated actions
last_action_time = 0
delay = 1

def count_fingers(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in fingerTips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            finger_count = count_fingers(handLms)
            current_time = time.time()

            if current_time - last_action_time > delay:

                if finger_count == 2:
                    pyautogui.press('right')
                    cv2.putText(img, "Next Slide", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    last_action_time = current_time

                elif finger_count == 3:
                    pyautogui.press('left')
                    cv2.putText(img, "Previous Slide", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    last_action_time = current_time

                elif finger_count == 5:
                    pyautogui.hotkey('ctrl', '+')
                    cv2.putText(img, "Zoom In", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    last_action_time = current_time

                elif finger_count == 0:
                    pyautogui.hotkey('ctrl', '-')
                    cv2.putText(img, "Zoom Out", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    last_action_time = current_time

    cv2.imshow("Gesture Controlled Presentation", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
