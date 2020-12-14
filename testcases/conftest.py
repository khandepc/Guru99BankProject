
from selenium import webdriver
from utilities.custom_logger import LogGen
import pytest


log=LogGen.log_gen()
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        driver.maximize_window()
        log.info("Chrome browser launched...")
    elif browser=="firefox":
        driver=webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
        driver.maximize_window()
        log.info("firefox browser launched...")
    elif browser=="ie":
        driver=webdriver.Ie(executable_path="./drivers/IEDriverServer.exe")
        driver.maximize_window()
        log.info("ie browser launched...")
    elif browser=="opera":
        driver=webdriver.Opera(executable_path="./drivers/operadriver.exe")
        driver.maximize_window()
        log.info("opera browser launched...")
    else:
        driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        driver.maximize_window()
        log.info("chrome browser launched bydefault...")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


    def identify_element(self,locater_type,address):
        driver=setup
        element=None
        wait=WebDriverWait(self.driver,20,1)
        if locater_type=="id":
            locater=By.ID,address
            condition=ec.presence_of_element_located(locater)
            element=wait.until(condition)
            return element
        elif locater_type=="name":
            locater = By.NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="classname":
            locater = By.CLASS_NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="tagname":
            locater = By.TAG_NAME, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="linktext":
            locater = By.LINK_TEXT, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="partiallinktext":
            locater = By.PARTIAL_LINK_TEXT, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="css":
            locater = By.CSS_SELECTOR, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type=="xpath":
            locater = By.XPATH, address
            condition = ec.presence_of_element_located(locater)
            element = wait.until(condition)
            return element
        else:
            log.error("invalid locater type")

    def explicitwaitmethod(self,condition,address,extra= None):
        wait = WebDriverWait(self.driver,20)
        element = None
        locator = By.XPATH, address
        if condition == 'visibility':
            cc = ec.visibility_of_element_located(locator)
            element = wait.until(cc)
        elif condition == 'title':
            cc = ec.title_contains(extra)
            element=wait.until(cc)
        return element


    def identify_elements(self,locater_type,address):
        element=None
        wait=WebDriverWait(self.driver,20,1)
        if locater_type == "id":
            locater = By.ID, address
            condition=ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "name":
            locater = By.NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "classname":
            locater = By.CLASS_NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "tagname":
            locater = By.TAG_NAME, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "linktext":
            locater = By.LINK_TEXT, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "partiallinktext":
            locater = By.PARTIAL_LINK_TEXT, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "css":
            locater = By.CSS_SELECTOR, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        elif locater_type == "xpath":
            locater = By.XPATH, address
            condition = ec.presence_of_all_elements_located(locater)
            element = wait.until(condition)
            return element
        else:
            log.error("invalid locater type")