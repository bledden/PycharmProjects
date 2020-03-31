from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_id("exampleCheck1").click()  # Click on the checkbox
driver.find_element_by_name("name").send_keys("Blake")  # Searches in HTML for the property "name" and sends the value to it
driver.find_element_by_id("exampleInputPassword1").send_keys("Test")
#  driver.find_element_by_css_selector("input[name='name']").send_keys("Blake")  # Has 2 cases of it (proven by entering input[name='name'] into html inspect element console; this populates both locations
driver.find_element_by_name("email").send_keys("nonyabidness@nope.com")
# ^Selenium searches css for elements that match what you have prompted it to starting at the top left corner of the webpage (0,0) and working down right
driver.find_element_by_id("exampleCheck1").click()  # Unclicks the box
driver.find_element_by_id("inlineRadio1").click()
driver.find_element_by_name("bday").send_keys("06-09-1994")  # This is the date input format even though html range is "YYYY-MM-DD"
# driver.find_element_by_id("exampleFormControlSelect1").
driver.find_element_by_id("inlineRadio2").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)  # This prints the message on the page
# //*[contains(@class,'aler-success')] - Xpath
# [class*='alert-success']  - CSS

# Below is an unnecessary script I made to see if I could
successCheck = driver.find_element_by_class_name("alert-success").text
# It pulls the string from the designated class object created above and makes it a list object
hold = successCheck.split()
# The below for loop then searches through each item for the word "Success!"
# If it finds it, it prints a "Complete!" message and breaks the loop, if it fails, it says "Not quite"
for i in range(0, len(hold) - 1):
    if hold[i] == "Success!":
        print("Complete!")
        break
    else:
        print("Not quite")




# driver.quit()
