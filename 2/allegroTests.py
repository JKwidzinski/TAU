from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
import time
import logging

logging.basicConfig(filename='allegroTestsLog.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def ChromeSearchTshirtTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logging.info('Going to allegro.pl')
    driver.get("https://allegro.pl/")   
    
    try:
        logging.info('Accepting cookies')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        logging.info('Searching for koszulka')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        element.clear()
        element.send_keys("koszulka")
        element.send_keys(Keys.ENTER)
        
        assert 'szukasz „koszulka”' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')

def ChromeChangeLanguageTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logging.info('Going to allegro.pl')
    driver.get("https://allegro.pl/")   
    
    try:
        logging.info('Accepting cookies')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        logging.info('Editing localization options')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@data-analytics-click-label="ShippingCountryFlag"]')))
        element.click()
        
        logging.info('Switching language to EN')
        select_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'language-select')))
        select_object = Select(select_element)
        select_object.select_by_value("en-US")
        
        logging.info('Confirming changes')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Zmień"]')))
        element.click()
        
        assert 'Categories' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')
        
def FirefoxSearchTshirtTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    logging.info('Going to allegro.pl')
    driver.get("https://allegro.pl/")   
    
    try:
        logging.info('Accepting cookies')       
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        logging.info('Searching for koszulka')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        element.clear()
        element.send_keys("koszulka")
        element.send_keys(Keys.ENTER)
        
        assert 'szukasz „koszulka”' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')

def FirefoxChangeLanguageTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    logging.info('Going to allegro.pl')
    driver.get("https://allegro.pl/")   
    
    try:
        logging.info('Accepting cookies')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        logging.info('Editing localization options')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@data-analytics-click-label="ShippingCountryFlag"]')))
        element.click()
        
        logging.info('Switching language to EN')
        select_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'language-select')))
        select_object = Select(select_element)
        select_object.select_by_value("en-US")
        
        logging.info('Confirming changes')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Zmień"]')))
        element.click()
        
        assert 'Categories' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')


def main():
    ChromeSearchTshirtTest()
    ChromeChangeLanguageTest()
    FirefoxSearchTshirtTest()
    FirefoxChangeLanguageTest()
    
if __name__ == '__main__':
    main()