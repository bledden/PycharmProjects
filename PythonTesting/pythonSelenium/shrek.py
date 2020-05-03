#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Variables
facebookEmail = "Put it here"
facebookPassword = "Put it here"
friendName = "Put person here"
sendDelay = 1;

# Opens Facebook Messenger
driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get('https://www.messenger.com/')

# Login
driver.find_element_by_id("close").click()
driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebookEmail)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebookPassword)
driver.find_element_by_id("loginbutton").click()

# Gets user from conversation list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

# Reads Shrek script file and saves to movie_script list
movie_script = []
with open('script.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            insertMessage = driver.find_element_by_class_name('_1mj')
            insertMessage.send_keys(word, Keys.ENTER)
            time.sleep(sendDelay)




