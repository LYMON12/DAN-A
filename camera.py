import time
import numpy as np
import cv2
import keyboard as kb
import subprocess as sp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#import mediapipe as mp
fonte = cv2.FONT_HERSHEY_SIMPLEX 

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
        #cv2 .putText ( img_rosto , ' LIMAO_GOSTOSO ' , ( 10,500 ) , fonte , 4 , ( 255,0,0 ) , 2 , cv2.LINE_AA )

#LEITURA-OLHO    
    leitura_olho = olho.detectMultiScale(gray)
    for (ox,oy,ow,oh) in leitura_olho:
        img_olho = cv2.rectangle(frame,(ox,oy),(ox+ow,oy+oh),(155,17,30),2)
 
    if len(leitura_rosto) > 0:
       sp.Popen(["notepad.exe"])
       time.sleep(3)
       sp.getoutput()
       kb.write('BEM BONITIN')

     

#MOSTRAR-IMAGEM
    #cv2.imshow('frame', gray)
    cv2.imshow('img_rosto',frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
