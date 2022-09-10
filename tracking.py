import cv2
import mediapipe as mp

vid = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

def drawhandlandmarks(img,hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(img,landmarks,mp_hands.HAND_CONNECTIONS)


while True:
    success, img = vid.read()
    img = cv2.flip(img,1)
    results = hands.process(img)
    hand_landmarks = results.multi_hand_landmarks
    drawhandlandmarks(img,hand_landmarks)
    cv2.imshow("label",img)
    key = cv2.waitKey(1)
    
    if key == 32:
        break

cv2.release()
cv2.destroyAllWindows()