from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.custom_logger import LogGen

log=LogGen.log_gen()
class SeleniumBase:


    def __init__(self,driver):
        self.driver=driver


    def identify_element(self,locater_type,address):
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