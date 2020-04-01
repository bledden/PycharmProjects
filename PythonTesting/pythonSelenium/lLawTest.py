# Hi! This was made by Blake Ledden


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get("https://www.google.com/")
# driver.maximize_window()
driver.find_element_by_name("q").send_keys("Luke Lawrence")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[0].click()
driver.find_element_by_id("email").send_keys("blakesprogramming@gmail.com")
driver.find_element_by_id("pass").send_keys("GenericShit33%")
driver.find_element_by_name("pass").send_keys(Keys.RETURN)
driver.get("https://www.facebook.com/THE.CHUBBY.EMINEM/")
driver.get("https://www.facebook.com/THE.CHUBBY.EMINEM/")

# Have yet to figure out how to get his exact page to pull up with a click
# Was on to something using Chropath to find his url ID, but it kept pulling up the third Luke Lawrence


