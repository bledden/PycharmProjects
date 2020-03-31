# Hi! This was made by Blake Ledden
# This is a Selenium script in python to perform a google search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver")
driver.get("https://www.google.com/")
# driver.maximize_window()
driver.find_element_by_name("q").send_keys("Blake Ledden")
driver.find_element_by_name("q").send_keys(Keys.RETURN)  # Performs the Google Search
