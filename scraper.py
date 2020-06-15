from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

HOME = 'https://www.instagram.com'
LOGIN = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

def sleep_wrap(func, sleep, *args, **kwargs):
    time.sleep(sleep)
    func(*args, *kwargs)
    time.sleep(sleep)

def login(driver,username,password):
    sleep_wrap(go,3,driver,LOGIN)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')
    sleep_wrap(go,3,driver,HOME)
    NEXT_BUTTON_XPATH = "//button[@class='aOOlW   HoLwm ']"
    button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
    button.click()

def go(driver, link, sleep=3):
    driver.get(link)

def get_loc(driver, loc):
    sleep_wrap(go,3,driver,HOME)
    input_search = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'XTCLo')]")))
    sleep_wrap(input_search.send_keys, 1, loc)
    sleep_wrap(input_search.send_keys, 2, Keys.ENTER)
    sleep_wrap(input_search.send_keys, 3, Keys.ENTER)
    print(driver.current_url)
    return driver.current_url
