from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class InstaScraper:
    '''
    Geo Scraper
    
    HOME    : Homepage for queries
    LOGIN   : OAuth Page
    LOGGED  : Check if logged in

    init    : start browser
    login   : pass username and password

    '''
    def __init__(self):
        self.HOME = 'https://www.instagram.com'
        self.LOGIN = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        self.LOGGED = False
        self.init()
    
    def init(self):
        self.driver=webdriver.Chrome()
    
    def login(self,username,password):
        '''
        LOGIN INSTAGRAM USING YOUR ID AND PASSWORD

        username : Instagram Username
        password : Instagram Password
        '''
        # LOGIN
        self.go(self.LOGIN)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password").send_keys(u'\ue007')
        self.logged=True
        time.sleep(5)
        
        # GOTO HOMEPAGE AND TACKLE INITIAL DIALOG BOXES
        self.go(self.HOME)
        NEXT_BUTTON_XPATH = "//button[@class='aOOlW   HoLwm ']"
        button = self.driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
        button.click()
        time.sleep(5)

    def go(self, link):
        '''
        GET LINK

        link    : URL you want your browser to go to
        '''
        self.driver.get(link)
        time.sleep(5)

    def get_loc(self, loc):
        '''
        LOCATION EXTRACTOR

        loc     : Name of query
        '''
        # Reach Homepage
        self.go(self.HOME)
        
        #Collect search box, clear, enter query, click
        search_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'XTCLo')]")))
        search_box.clear()
        search_box.send_keys(loc)
        time.sleep(5)
        search_box.send_keys(Keys.ENTER)
        time.sleep(0.5)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

        #LOG OUTPUT
        print(self.driver.current_url)

        #RETURN LINK
        return self.driver.current_url