# Hi! This was made by Blake Ledden


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Safari()

driver.get("https://login.salesforce.com")
driver.find_element_by_id("username").send_keys("RickSanchez42")
driver.find_element_by_id("password").send_keys("Lololololololnope12%")
driver.find_element_by_id("Login").click()
