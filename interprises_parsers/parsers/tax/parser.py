import os, sys
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_anticaptcha import AnticaptchaClient, ImageToTextTask


api_key = "49c1b7251a620fab81efd5a39eda9673"

uin = sys.argv[1]


def __settings():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    phantomjs = os.path.join(SITE_ROOT, "static", "phantomjs")

    browser = webdriver.PhantomJS(executable_path=phantomjs)
    browser.set_window_size(1366, 768)
    return browser

browser = __settings()

def get_captcha(browser, element, path):
    location = element.location
    size = element.size

    browser.save_screenshot(path)

    image = Image.open(path)

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    image = image.crop((left, top, right, bottom))
    image.save(path, 'png')
    
def process(path):
    captcha_fp = open(path, 'rb')
    client = AnticaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task)
    job.join()
    return job.get_captcha_text()


browser.get("http://kgd.gov.kz/ru/services/taxpayer_search/legal_entity")

img = browser.find_element_by_id("imageCaptcha")
get_captcha(browser, img, uin+".png")

solved = str(process(uin+".png"))

browser.find_element_by_id("edit-uin").send_keys(uin)
browser.find_element_by_id("edit-entercaptcha").send_keys(solved)
browser.find_element_by_id("edit-submit").click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form table"))
    )
except:
    browser.quit()
    print(0);
    sys.exit()

tables = browser.find_elements_by_css_selector("form table")

for table in tables:
    print(table.get_attribute('outerHTML'))
    

browser.quit()







     
    
    
