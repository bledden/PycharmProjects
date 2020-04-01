from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get("https://www.google.com/")
# driver.maximize_window()
driver.find_element_by_name("q").send_keys("Jarrett Wangsnes")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[1].click()
driver.find_element_by_id("email").send_keys("blakesprogramming@gmail.com")
driver.find_element_by_id("pass").send_keys("GenericShit33%")
driver.find_element_by_name("pass").send_keys(Keys.RETURN)
driver.get("https://www.facebook.com/jarrett.wangsnes")
driver.get("https://www.facebook.com/jarrett.wangsnes")
driver.find_element_by_id("u_0_1b").click()
# driver.find_element_by_xpath("//div[@class=f'_552h']").click()
# driver.find_element_by_xpath('//div[@class="_552h"]').send_keys("Sup noob")
# driver.find_element_by_xpath('//textarea[@class="uiTextareagrow _552"]').send_keys("sup noob")
# driver.find_element_by_id("cch_fa5631d53fb9f4").click()
# driver.find_element_by_id("cch_fa5631d53fb9f4").send_keys("Sup noob")
# driver.find_element_by_xpath('//div[@id="placeholder-96vh4"]')
# mssgbox = driver.find_element_by_css_selector("textarea[class*='uiTextareaAutogrow _552m']")
# mssgbox.click()
# mssgbox.send_keys("Sup noob")
