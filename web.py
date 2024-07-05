import time
import keyboard as kb
import subprocess as sp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sp.Popen(["notepad.exe"])
time.sleep(3)
kb.write('BEM BONITIN')
#site = webdriver.Chrome()
#local = site.get("https://pt.anotepad.com/")
#time.sleep(3)

#bandeira_verde = site.find_element(By.ID, "edit_title")
#bandeira_verde.click()
#site.current_window_handle()
#kb.press('a')
#if len(local) > 0:
   #kb.press("a")