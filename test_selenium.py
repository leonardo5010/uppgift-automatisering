import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MinaTester(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.mediamarkt.se/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR,"body > div.gdpr-cookie-layer.gdpr-cookie-layer--show > div > div.gdpr-cookie-layer__lower-section > div.gdpr-cookie-layer__submit-buttons > button.gdpr-cookie-layer__btn.gdpr-cookie-layer__btn--submit.gdpr-cookie-layer__btn--submit--all").click()

    def test_kundservice_(self):
        self.driver.find_element(By.XPATH, '//*[@id="rise-header"]/div[1]/nav[1]/ul/li[1]/a').click()
        #Kundservice = self.driver.find_element(By.XPATH, '//*[@id="yui_3_18_1_6_1679582939285_6"]/div[3]/div[2]').text
        expected = 'https://kundservice.mediamarkt.se/'
        url = self.driver.current_url
        self.assertEqual(url, expected) 


# våra tjänster, det ska vara enkelt att komma till oss
    def test_vara_tjanster(self):
        self.driver.find_element(By.XPATH, '//*[@id="rise-header"]/div[1]/nav[2]/div[1]/ul/li[4]/a/span').click() 
        self.driver.execute_script("scrollBy(0,300)")
        time.sleep(3)
        vara_tjanster = self.driver.find_element(By.XPATH, '//*[@id="servicemall-advanced"]/header/div[2]/h1').text 
        expected = 'Det ska vara enkelt att komma till oss'
        self.assertEqual(vara_tjanster, expected)

    # Verifiera att det står "Våra aktuella kampanjer" när man klickat i kampanj
    def test_kampanjer(self):
        self.driver.find_element(By.XPATH, '//*[@id="rise-header"]/div[1]/nav[2]/div[1]/ul/li[3]/a/span').click()
        kampanjer = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[11]/div/section/h1').text
        expected = 'VÅRA AKTUELLA KAMPANJER'
        self.assertEqual(kampanjer, expected)

   # Verifiera att det står Retur / Återköp
    def test_retur_aterkop(self):
        self.driver.execute_script("scrollBy(0,1000)")
        self.driver.find_element(By.XPATH, '//*[@id="page-footer"]/div[1]/div/div[2]/div/ul/li[6]/a').click()
        retur_aterkap = self.driver.find_element(By.XPATH, '//*[@id="servicemall"]/header/div[2]/h1').text
        expected = 'Retur / Återköp'
        self.assertEqual(retur_aterkap, expected)

#Outlet hemsidan öppnas
    def test_outlet(self):
        self.driver.find_element(By.XPATH, '//*[@id="rise-header"]/div[1]/nav[2]/div[1]/ul/li[6]/a/span').click()
        outlet = self.driver.find_element(By.XPATH, '//*[@id="search_campaign_outlet_1-top_right"]/div[2]/article/p').text
        expected = 'PS. Alla produkter i Outleten är helt nya, dvs inte returer eller visningsexemplar. Välkommen att fynda!'
        self.assertEqual(outlet, expected)
    