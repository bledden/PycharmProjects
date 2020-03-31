# Hi! This was made by Blake Ledden

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()  # Safari does not need an executable because Mac rulez

driver.get("https://www.google.com/")  # Opens the browser
driver.find_element_by_name("q").send_keys("Blake Ledden")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
print(driver.title)  # Prints name of url reacher
print(driver.current_url)  # Prints out the current url address
# driver.close()  # Closes child window
# driver.quit()  #Thiscloses all windows
