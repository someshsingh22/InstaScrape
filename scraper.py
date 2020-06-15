from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

HOME = 'https://www.instagram.com'
LOGIN = 'https://www.instagram.com/accounts/login/?source=auth_switcher'

def sleep_wrap(func, sleep, *args, **kwargs):
    time.sleep(sleep)
    out=func(*args, *kwargs)
    time.sleep(sleep)
    return out

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

def get_loc(driver, loc, list):
    sleep_wrap(go,3,driver,HOME)
    input_search = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'XTCLo')]")))
    input_search.clear()
    sleep_wrap(input_search.send_keys, 0.5, loc)
    sleep_wrap(input_search.send_keys, 4, Keys.ENTER)
    sleep_wrap(input_search.send_keys, 4, Keys.ENTER)
    print(driver.current_url)
    return driver.current_url

if __name__ == "__main__":

    #If running as a part of a module uncomment the line below
    #from scraper import *
    from selenium import webdriver
    import pandas as pd
    browser = webdriver.Chrome()
    sleep_wrap(login, 3, browser, "somesh.22", "someshSINGH@22")
    links = []
    csv = pd.read_csv('insta.csv')
    locations = (csv['Apartment Name']+csv['City']).tolist()
    for loc in locations:
        try:
            links.append(sleep_wrap(get_loc, 0.5, browser, loc))
        except:
            links.append("NA")
    csv['Links']=links
    csv.to_csv('insta_locs.csv', index=False)