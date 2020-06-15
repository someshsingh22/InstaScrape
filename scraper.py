from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

HOME = 'https://www.instagram.com'
LOGIN = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

def sleeper(sleep=3):
    def decorator(action):
        def wrapper(*args, **kwargs):
            time.sleep(sleep)
            action(*args, **kwargs)
            time.sleep(sleep)
        return wrapper
    return decorator

@sleeper(sleep=1)
def login(driver,username,password,sleep=3):
    go(driver,LOGIN)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')
    go(driver,HOME)
    NEXT_BUTTON_XPATH = "//button[@class='aOOlW   HoLwm ']"
    button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
    button.click()

@sleeper
def go(driver, link, sleep=3):
    driver.get(link)
