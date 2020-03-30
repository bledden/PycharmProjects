from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Blake")  # Searches in HTML for the property "name" and sends the value to it
driver.find_element_by_id("exampleInputPassword1").send_keys("Test")
