from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome()
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver.get_cookies())
