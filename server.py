import cv2
import socket
import mediapipe as mp
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(2)
clientsocket, adress = s.accept()


cap = cv2.VideoCapture(0)
cap.set(3, 700)
cap.set(4, 500)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    nincskez = True
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                if id == 8:
                    if 700/2 < cx < 700:
                        balkez = cy
                        nincskez = False
                    
                
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                if id == 8:
                    if 700/2 > cx < 700:
                        jobbkez = cy
                        nincskez = False
    if nincskez == True:
        balkez = 225
        jobbkez = 225
    adat = (balkez,jobbkez)
        
    if clientsocket:
        clientsocket.send(bytes(str(adat), 'utf-8'))
    #cv2.imshow('image', img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()