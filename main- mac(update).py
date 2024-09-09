from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import pyautogui as auto
import time
from threading import Thread

def start(input1,input2,input3,input4,input5,input6):
    # Get the correct path to the .crx file after the app is bundled
    # if hasattr(sys, '_MEIPASS'):
    #     crx_path = os.path.join(sys._MEIPASS, 'extension.crx')
    # else:
    #     crx_path = 'your extension path'  # add your extension path

    options = Options()
    options.add_extension("extension.crx")
    driver = Chrome(options=options)
    driver.get('https://www.cpwshop.com/home.page')
    driver.maximize_window()
    time.sleep(8)
    driver.find_element(By.XPATH,'//*[@id="loginMenuWrapper"]').click() # Sign in button
    time.sleep(3)
    inputfields = driver.find_elements(By.TAG_NAME,'input')
    inputfields[0].send_keys(input1)
    inputfields[1].send_keys(input2)
    driver.find_element(By.XPATH,'//*[@id="submit"]').click() #sign in button
    time.sleep(6)
    driver.find_element(By.XPATH,'//*[@id="submit"]').click() #confirm details
    time.sleep(6)
    driver.get('https://www.cpwshop.com/purchaseprivilege.page?_PageParam.displayCategoryID=251534295')
    time.sleep(2)


    count = 0
    
    print(driver.find_element(By.XPATH,'//*[@id="selectResidency-title"]').text)
    inputfields = driver.find_elements(By.TAG_NAME,'input')
    inputfields[0].click() #selecting
    time.sleep(2)
    inputfields[1].send_keys('032002')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="submit"]').click()
    time.sleep(8)

    driver.find_elements(By.CLASS_NAME,'collapsed')[1].click()
    time.sleep(2)
    buttons = driver.find_elements(By.CLASS_NAME,'action') #Purchase
    for i in buttons:
        print(i.text)
    buttons[3].click()
    time.sleep(2)
    textfield = driver.find_elements(By.TAG_NAME,'input')
    textfield[1].send_keys(input3)
    time.sleep(1)
    textfield[2].send_keys(input4)
    time.sleep(1)
    textfield[3].send_keys(input5)
    time.sleep(1)
    textfield[4].send_keys(input6)
    time.sleep(1)
    def keepcheckingcart():
        while True:
            time.sleep(0.2)
            try:
                anchor = driver.find_elements(By.TAG_NAME,'a')
                for i in anchor:
                    if i.text == "Add to Cart":
                        i.click()
            except:
                print("cart not present yet")
    th = Thread(target=keepcheckingcart)
    th.start()
    while True:
        if count == 0:
            driver.find_element(By.ID,'GoogleReCaptchaNextBtnContainer').click() #Captcha checkbox
            time.sleep(3)
            try:
                auto.click(713,854)
                time.sleep(1)
                confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm Choices")))
                confirm_button.click()  # Click the "Confirm Choices" button
                print("Button clicked successfully.")
            except:
                pass                            
            count = count + 1
        else:
            auto.click(713,854)
            time.sleep(1)
            try:
                confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm Choices")))
                confirm_button.click()  # Click the "Confirm Choices" button
                print("Button clicked successfully.")
            except:
                try:
                    # Handle captcha if needed
                    captchabox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'GoogleReCaptchaNextBtnContainer')))
                    captchabox.click()  # Click captcha checkbox
                    print("Captcha clicked, retrying button click.")
                except Exception as e:
                    print("Error with captcha:", e)

