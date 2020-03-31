from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get("https://facebook.com/")
driver.find_element_by_id("email").send_keys("blakesprogramming@gmail.com")
driver.find_element_by_id("pass").send_keys("GenericShit33%")
driver.find_element_by_name("pass").send_keys(Keys.RETURN)
# driver.find_element_by_name("xhpc_message_text").send_keys("If this posts, my script works!")
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable(By.xpath("//button/span[.=\"Post\"]"))).click()



