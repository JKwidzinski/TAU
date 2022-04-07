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

def ChromeSearchTshirtTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://allegro.pl/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        element.clear()
        element.send_keys("koszulka")
        element.send_keys(Keys.ENTER)
        
        assert 'szukasz „koszulka”' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()

def ChromeChangeLanguageTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://allegro.pl/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@data-analytics-click-label="ShippingCountryFlag"]')))
        element.click()
        
        select_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'language-select')))
        select_object = Select(select_element)
        select_object.select_by_value("en-US")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Zmień"]')))
        element.click()
        
        assert 'Categories' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()
        
def FirefoxSearchTshirtTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://allegro.pl/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
        element.clear()
        element.send_keys("koszulka")
        element.send_keys(Keys.ENTER)
        
        assert 'szukasz „koszulka”' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()

def FirefoxChangeLanguageTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://allegro.pl/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@data-role="accept-consent"]')))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@data-analytics-click-label="ShippingCountryFlag"]')))
        element.click()
        
        select_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'language-select')))
        select_object = Select(select_element)
        select_object.select_by_value("en-US")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Zmień"]')))
        element.click()
        
        assert 'Categories' in driver.page_source
        time.sleep(10)
        driver.quit()
    except:
        driver.quit()


def main():
    ChromeSearchTshirtTest()
    ChromeChangeLanguageTest()
    FirefoxSearchTshirtTest()
    FirefoxChangeLanguageTest()
    
if __name__ == '__main__':
    main()