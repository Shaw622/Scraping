import time
import pytesseract
from urllib.request import urlretrieve
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/dp/1427027277')
time.sleep(2)

# Click on the book preview button
driver.find_element_by_id('imgBlkFront').click()
imageList = []

# Wait for the page to load
time.sleep(5)

while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    # While the right arrow is available for clicking, turn through pages
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # Get any new pages that have loaded (multiple pages can load at once,
    # but duplicates will not be added to a set)
    pages = driver.find_elements_by_xpath(
        '//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print('No pages found')
    for page in pages:
        image = page.get_attribute('src')
        print('Found image: {}'.format(image))
        if image not in imageList:
            urlretrieve(image, 'page.jpg')
            imageList.append(image)
            print(pytesseract.image_to_string(Image.open('page.jpg')))

driver.quit()
