import os
import time
import pathlib
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#so many imoports lol fuck uselenium

path = pathlib.Path().resolve() #gets current path

check = os.path.isfile(f"{path}\chromedriver.exe") #checks if chromedriver is in the current path
if check == False: #returns false if its not
    print("Please put chromedriver into the current directory!") #put it in ur directory 
else:
    msg = input("|+| Message to send => ") #msage to send

    PATH = f"{path}\chromedriver.exe" #gets path for chrmoedrvier

    driver = webdriver.Chrome(PATH) #initializing driver 
    driver.get("https://omegle.com") #get driver for site
    
    time.sleep(2)

    text = WebDriverWait(driver, 10).until( #waits 10 seconds
    EC.presence_of_element_located((By.ID, "textbtn")) #for textbtn to be present in html
    )

    text.click() #clicks it

    driver.find_element_by_xpath("//label/input[contains(..,'Terms of Service')]").click() #clicks button lol
    driver.find_element_by_xpath("//label/input[contains(..,' for more info. ')]").click() #clicks button lol

    button1 = driver.find_element_by_xpath("//body/div[7]/div[1]/p[3]/input[1]") 
    button1.click() #clicks another button bruh
    
while True:
        message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "chatmsg")) #find box u use to input message
        )

        try:
            message.send_keys(msg) #send string to class "chatmsg" the chatbox for omegle
            message.send_keys(Keys.RETURN) #keys presses return aka "enter"
        except:
            pass
        else:
            new = WebDriverWait(driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "disconnectbtn")) #presses dsconected buton
            )
            
            for i in range(3):
                new.click() #clicks end buttttonon
                time.sleep(0.2)
