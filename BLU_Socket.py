import socket as sk
import bleak 
from bleak import BleakScanner

async def achar_porta():
      portas = await BleakScanner.discover()
      for porta in portas:
          print(f"encontrado: {porta.name} - {porta.address}")  

StopAsyncIteration()

#sk.AF_BLUETOOTH()
