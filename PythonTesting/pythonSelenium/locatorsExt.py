# Hi! This was made by Blake Ledden

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path="/Users/starlord/chromedriver", options=chrome_options)
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Something")
driver.find_element_by_css_selector(".password").send_keys("Shapoopy69")
# driver.find_element_by_css_selector("#Login").click()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
driver.find_element_by_xpath("//form[@name='login']/div[1]/label")


