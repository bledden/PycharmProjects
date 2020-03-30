# Hi! This was made by Blake Ledden

from selenium import webdriver

# Browser exposes an executable file
# Through Selenium we will invoke the executable file which will then invoke the browser itself
# driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver")  # This is the file path for the chrome driver
driver = webdriver.Firefox(executable_path="/Users/starlord/geckodriver") # This test Firefox instead of Chrome
driver.maximize_window()
driver.get("https://www.google.com/")  # Get method to hit url on browser

print(driver.title)
print(driver.current_url)
driver.get("https://reddit.com")
driver.back()
driver.minimize_window()
driver.refresh()
driver.quit()  # driver.quit() may be preferable unless getting specific or testing a specific page/section of a site
# driver.close() <-- May be better for debugging
