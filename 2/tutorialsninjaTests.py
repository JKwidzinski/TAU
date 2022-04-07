from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import logging

#Email needs to be changed in order to register account(acc with this email exists)
def ChromeRegisterTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-firstname")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-lastname")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-telephone")))
        element.clear()
        element.send_keys("123123123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-confirm")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "agree")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "Your Account Has Been Created!" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()
        
def ChromeLoginTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "My Affiliate Account" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()

#Email needs to be changed in order to register account(acc with this email exists)        
def FirefoxRegisterTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://tutorialsninja.com/demo/")
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-firstname")))
        element.clear()
        element.send_keys("123asd")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-lastname")))
        element.clear()
        element.send_keys("123asd")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("123asd@wp.pl")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-telephone")))
        element.clear()
        element.send_keys("321321321")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("123asd")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-confirm")))
        element.clear()
        element.send_keys("123asd")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "agree")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "Your Account Has Been Created!" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()        
        
def FirefoxLoginTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        element.click()
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "My Affiliate Account" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()

def main():
    ChromeRegisterTest()
    ChromeLoginTest()
    FirefoxRegisterTest()
    FirefoxLoginTest()
    

if __name__ == '__main__':
    main()    