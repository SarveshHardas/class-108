import cv2
import mediapipe as mp

vid = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
tipids = [4,8,12,16,20]

def drawhandlandmarks(img,hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(img,landmarks,mp_hands.HAND_CONNECTIONS)

def countfinger(img,hand_landmarks,handnumber = 0):
    if hand_landmarks:
        landmarks = hand_landmarks[handnumber].k=landmark
        finger = []
        for i in tipids:
            finger_tip_y = landmarks[i].y
            finger_bottom_y = landmarks[i-2].y
            
            if i !=4:
                if finger_tip_y<finger_bottom_y:
                    finger.append(1)
                    print('finger is open')

                if finger_tip_y>finger_bottom_y:
                    finger.append(0)
                    print('finger is closed')

        totalfinger = finger.count(1)
        text = f'finger:{totalfinger}'
        cv2.putText(img,text,(50,50),cv2.FONT_HARSHEY_SIMPLEX,1,(255,0,0),2)





while True:
    success, img = vid.read()
    img = cv2.flip(img,1)
    results = hands.process(img)
    hand_landmarks = results.multi_hand_landmarks

    drawhandlandmarks(img,hand_landmarks)
    countfinger(img,hand_landmarks)
    
    cv2.imshow("label",img)
    key = cv2.waitKey(1)
    
    if key == 32:
        break

cv2.release()
cv2.destroyAllWindows()