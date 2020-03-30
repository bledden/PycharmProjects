# Hi! This was made by Blake Ledden

from selenium import webdriver

driver = webdriver.Safari()  # Safari does not need an executable because Mac rulez

driver.get("https://www.google.com/")  # Opens the browser

print(driver.title)  # Prints name of url reacher
print(driver.current_url)  # Prints out the current url address
# driver.close()  # Closes child window
driver.quit()  #Thiscloses all windows
