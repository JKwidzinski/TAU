from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import logging

logging.basicConfig(filename='testLog.log', level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger('task')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class TestSelenium():
    
    @pytest.fixture()
    def setup(self):
        global driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_register(self, setup):
        logging.info('Go to tutorialsninja')
        self.driver.get("http://tutorialsninja.com/demo")
        
        logging.info('Dropdown toggle')
        self.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle").click()
        
        logging.info('Click Register')
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        
        logging.info('Input firstname')
        self.driver.find_element(By.ID, "input-firstname").send_keys('cxz321')
        
        logging.info('Input lastname')
        self.driver.find_element(By.ID, "input-lastname").send_keys('cxz321')
        
        logging.info('Input email')
        self.driver.find_element(By.ID, "input-email").send_keys('cxz321@wp.pl')
        
        logging.info('Input telephone')
        self.driver.find_element(By.ID, "input-telephone").send_keys('321321321')
        
        logging.info('Input password')
        self.driver.find_element(By.ID, "input-password").send_keys('cxz321')
        
        logging.info('Input confirm password')
        self.driver.find_element(By.ID, "input-confirm").send_keys('cxz321')
        
        logging.info('Click agree to terms')
        self.driver.find_element(By.NAME, "agree").click()
        
        logging.info('Submit form')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        assert self.driver.title == "Your Account Has Been Created!"

    def test_login(self, setup):
        logging.info('Go to tutorialsninja')
        self.driver.get("http://tutorialsninja.com/demo")
        
        logging.info('Dropdown toggle')
        self.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle").click()
        
        logging.info('Click Login')
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        
        logging.info('Input email')
        self.driver.find_element(By.ID, "input-email").send_keys('cxz321@wp.pl')
        
        logging.info('Input password')
        self.driver.find_element(By.ID, "input-password").send_keys('cxz321')
        
        logging.info('Submit form')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        assert self.driver.title == 'My Account'
        
    def test_change_password(self, setup):
        logging.info('Go to tutorialsninja')
        self.driver.get("http://tutorialsninja.com/demo")
        
        logging.info('Dropdown toggle')
        self.driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle").click()
        
        logging.info('Click Login')
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        
        logging.info('Input email')
        self.driver.find_element(By.ID, "input-email").send_keys('cxz321@wp.pl')
        
        logging.info('Input password')
        self.driver.find_element(By.ID, "input-password").send_keys('cxz321')
        
        logging.info('Submit form')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        logging.info('Click change your password')
        self.driver.find_element(By.LINK_TEXT, "Change your password").click()
        
        logging.info('Input password')
        self.driver.find_element(By.ID, "input-password").send_keys('cxz123')
        
        logging.info('Input confirm password')
        self.driver.find_element(By.ID, "input-confirm").send_keys('cxz123')
        
        logging.info('Submit form')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        assert self.driver.find_element(By.XPATH, "//div[text()=' Success: Your password has been successfully updated.'").text == ' Success: Your password has been successfully updated.'