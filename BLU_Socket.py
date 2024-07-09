import socket as sk
#import bleak 
#from bleak import BleakScanner
import serial

s = serial.Serial('COM5', 9600, timeout = 1)
blu = s.in_waiting()

#---LOOP--------------
while True:
      s.write(b"Ola, Arduino")
      if blu > 0:
         s.write("Algo foi detectado")
      else:
           s.readline()
           print("Nada foi encontrado")

           break
s.flush()
