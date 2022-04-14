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

logging.basicConfig(filename='tutorialsNinjaTestsLog.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#Email needs to be changed in order to register account(acc with this email exists)
def ChromeRegisterTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logging.info('Going to tutorialsninja.com/demo')
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:
        logging.info('Opening dropdown')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        logging.info('Clicking Register')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        element.click()
        
        logging.info('Inputting first name')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-firstname")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Inputting lastname')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-lastname")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Inputting email')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        logging.info('Inputting telephone number')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-telephone")))
        element.clear()
        element.send_keys("123123123")
        
        logging.info('Inputting password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Inputting confirm password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-confirm")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Agreeing to terms')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "agree")))
        element.click()
        
        logging.info('Confirming registration')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "Your Account Has Been Created!" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')
        
def ChromeLoginTest():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logging.info('Going to tutorialsninja.com/demo')
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:
        logging.info('Opening dropdown')         
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        logging.info('Clicking Login')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        element.click()
        
        logging.info('Inputting email')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        logging.info('Inputting password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Confirming login process')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "My Affiliate Account" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')

#Email needs to be changed in order to register account(acc with this email exists)        
def FirefoxRegisterTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    logging.info('Going to tutorialsninja.com/demo')
    driver.get("http://tutorialsninja.com/demo/")
    
    try:
        logging.info('Opening dropdown')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        logging.info('Clicking Register')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        element.click()
        
        logging.info('Inputting first name')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-firstname")))
        element.clear()
        element.send_keys("123asd")
        
        logging.info('Inputting lastname')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-lastname")))
        element.clear()
        element.send_keys("123asd")
        
        logging.info('Inputting email')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("123asd@wp.pl")
        
        logging.info('Inputting telephone number')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-telephone")))
        element.clear()
        element.send_keys("321321321")
        
        logging.info('Inputting password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("123asd")
        
        logging.info('Inputting confirm password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-confirm")))
        element.clear()
        element.send_keys("123asd")
        
        logging.info('Agreeing to terms')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "agree")))
        element.click()
        
        logging.info('Confirming registration')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "Your Account Has Been Created!" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')       
        
def FirefoxLoginTest():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    logging.info('Going to tutorialsninja.com/demo')
    driver.get("http://tutorialsninja.com/demo/")   
    
    try:
        logging.info('Opening dropdown')        
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        element.click()
        
        logging.info('Clicking Login')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        element.click()
        
        logging.info('Inputting Email')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email")))
        element.clear()
        element.send_keys("asd123@wp.pl")
        
        logging.info('Inputting password')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-password")))
        element.clear()
        element.send_keys("asd123")
        
        logging.info('Confirming login process')
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        element.click()
        
        assert "My Affiliate Account" in driver.page_source
        time.sleep(20)
        driver.quit()
    except:
        driver.quit()
        logging.exception('Exception occured')

def main():
    ChromeRegisterTest()
    ChromeLoginTest()
    FirefoxRegisterTest()
    FirefoxLoginTest()
    

if __name__ == '__main__':
    main()    