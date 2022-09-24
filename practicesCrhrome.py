#!/usr/bin/python
#version: 2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import json
import time
import sys

        
with open("../practices/subjects.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file, )

username=sys.argv[1]
password=sys.argv[2]

print(">" + username + "<")
print(">" + password + "<")


#myOptions = webdriver.ChromeOptions()
#myOptions.add_arguments("disable-infobars")
#driver = webdriver.Chrome(options=myOptions)

driver = webdriver.Chrome("../practices/chromedriver.exe")

driver.get("https://www.dsi.uclm.es/logalumnx.php?que=login&XURL=%2Falumnos%2Fpracticas.php%3Fque%3Dau")


#WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.LINK_TEXT, "Pulsa aquí para autentificarte").click())

#Login
loginBox = WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.NAME, "txtloginUsr"))
loginBox.send_keys(username)

passwordBox = WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.NAME, "txtloginPwd"))
passwordBox.send_keys(password)

WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.NAME, "SubmitUsr").click())

#Storing links
links = []

#Save choosen subjects's links into list
for subject in data:  #For each subject in Json file
    for attribute in data[subject]:   #for each attribute in subject
        print(attribute["name"])
        links.append(WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.LINK_TEXT, attribute["name"])))

#Open links from variable link in new tabs                                                                      
for index in range(len(links)):
    driver.execute_script("window.open('{}');".format(links[index].get_attribute('href')))
    driver.switch_to.window(driver.window_handles[0]) 
    print(links[index].get_attribute('href'))
        

#driver.quit()





