import numpy as np
import cv2
#import mediapipe as mp

rosto = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
olho = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


cap = cv2.VideoCapture(0)
#rosto = mp.solutions.face_detection
#reconhecer = rosto.faceDetection

#if cap.isOpened():
    #print("Camera foi aberta")
    #exit()

if not cap.isOpened():
    print("Não foi possivel abrir a camera")
    exit()

while True:

    ret, frame = cap.read()

    #if ret:
        #print(" foi possivel receber a imagem...")
        #break

    if not ret:
        print("Não foi possivel receber a imagem...")
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#LEITURA-ROSTO
    leitura_rosto = rosto.detectMultiScale(gray, 1.1, 8)
    for (rx,ry,rw,rh) in leitura_rosto:
        img_rosto = cv2.rectangle(frame,(rx,ry),(rx+rw,ry+rh),(255,0,0),2)
        cinza = gray[ry:ry+rh, rx:rx+rw]

#LEITURA-OLHO    
    leitura_olho = olho.detectMultiScale(gray)
    for (ox,oy,ow,oh) in leitura_olho:
        img_olho = cv2.rectangle(frame,(ox,oy),(ox+ow,oy+oh),(155,17,30),2)


#MOSTRAR-IMAGEM
    #cv2.imshow('frame', gray)
    cv2.imshow('img_rosto',frame)
    
    if cv2.imshow("img_rosto",frame) == True: 
     print("FOIIII")

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()