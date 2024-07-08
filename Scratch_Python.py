import scratchattach as scratch3
import pyautogui, sys
import webbrowser
import requests
import time

#----COORDENADAS_MOUSE-------
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
#---------------------------

x, y = 891, 151

pyautogui.moveTo(x, y)
pyautogui.click()
time.sleep(10)
#session = scratch3.login("LIMAO_totoso", "Scratch2")
#projeto = session.connect_project("1045098565")
#projeto = session.connect_cloud("1045098565")

#projeto.set_title("Projeto_DANÇA")
