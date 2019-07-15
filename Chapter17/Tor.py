from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
driver = webdriver.Chrome(options=options)

driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()
