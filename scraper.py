from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver,username,password,sleep=3):
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(sleep)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')
    go_home(driver)
    NEXT_BUTTON_XPATH = "//button[@class='aOOlW   HoLwm ']"
    button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
    button.click()
    time.sleep(sleep)

def go_home(driver, sleep=3):
    time.sleep(sleep)
    driver.get('https://www.instagram.com')
    time.sleep(sleep)

    
