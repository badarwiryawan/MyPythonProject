#----------------------INPUT DAN RUNNING INI TERLEBIH DAHULU SECARA BERURUTAN DI COMMAND PROMPT. SESUAIKAN DIRECTORY-NYA----------------------------
#cd C:\Program Files\Google\Chrome\Application
#chrome.exe --remote-debugging-port=9393 chrome.exe --user-data-dir="D:\Programming\Chromeprofile"

import selenium
import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

os.environ['PATH']+="D:\Programming"
opt=Options()
tanggal = input("Masukkan Tanggal: ")

opt.add_experimental_option("debuggerAddress", "localhost:9393")
driver=webdriver.Chrome(options=opt)

driver.get("https://form.undip.ac.id/makanansehat/pendaftaran")
driver.implicitly_wait(10)
driver.find_element(By.ID, "select2-tanggal-container").click()
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys(tanggal)
time.sleep(1)
pyautogui.press('enter')
driver.find_element(By.CLASS_NAME, "ft-save").click()
time.sleep(1)
pyautogui.press('enter')










