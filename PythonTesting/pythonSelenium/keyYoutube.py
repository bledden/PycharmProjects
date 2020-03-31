from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

safari_options = Options()
safari_options.add_argument("--disable-notifications")

driver = webdriver.Safari()

driver.get("youtube.com")
