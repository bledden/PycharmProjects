#!/usr/bin/env python3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time



chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

twitterEmail = "blakesprogramm1"
twitterPassword = "GenericShit12$"
sendDelay = 2;

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get('https://twitter.com/login')

driver.implicitly_wait(10)
#driver.find_element_by_id("close").click()
driver.find_element_by_name("session[username_or_email]").send_keys(twitterEmail)
driver.find_element_by_name("session[password]").send_keys(twitterPassword)
driver.find_element_by_xpath('//div[@class="css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-vlx1xi r-zg41ew r-1jayybb r-17bavie r-1ny4l3l r-15bsvpr r-o7ynqc r-6416eg r-lrvibr"]//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"][contains(text(),"Log in")]').click()

movie_script = []
with open('gattaca.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            driver.find_element_by_xpath('//div[@class="css-1dbjc4n r-xoduu5 r-1sp51qo r-mk0yit r-13qz1uu"]').click()
            driver.find_element_by_xpath('//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys(word)
            driver.find_element_by_xpath('//span[@class="css-901oao css-16my406 css-bfa6kz r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"][contains(text(),"Tweet")]').click()
            time.sleep(sendDelay)

