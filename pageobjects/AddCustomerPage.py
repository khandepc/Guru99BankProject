
from utilities.custom_logger import LogGen

class AddCustomerPage:
    link_text_Add_new_customer_link="New Customer"
    xpath_customer_name_input_box="//input[@name='name']"
    xpath_gender_male="//input[@value='m']"
    xpath_gender_female="//input[@value='f']"
    xpath_date_of_birth_input_box="//input[@id='dob']"
    xpath_address_input_box="//textarea[@name='addr']"
    xpath_city_input_box="//input[@name='city']"
    xpath_state_input_box="//input[@name='state']"
    xpath_pin_no_input_box="//input[@name='pinno']"
    xpath_mobile_number_input_box="//input[@name='telephoneno']"
    xpath_email_id_input_box="//input[@name='emailid']"
    xpath_password_input_box="//input[@name='password']"
    xpath_submit_button="//input[@value='Submit']"
    xpath_reset_button="//input[@value='Reset']"

    logger=LogGen.log_gen()

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    def click_on_add_new_customer_link(self):
        self.driver.find_element_by_link_text(self.link_text_Add_new_customer_link).click()

    def set_customer_name(self,name):
        self.driver.find_element_by_xpath(self.xpath_customer_name_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_customer_name_input_box).send_keys(name)

    def click_on_gender_male(self,gender_type):
        if gender_type=="male":
            self.driver.find_element_by_xpath(self.xpath_gender_male).click()
        elif gender_type=="female":
            self.driver.find_element_by_xpath(self.xpath_gender_female).click()
        else:
            self.logger.error("Invalid gender type")

    def set_date_of_birth(self,dateofbirth):
        self.driver.find_element_by_xpath(self.xpath_date_of_birth_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_date_of_birth_input_box).send_keys(dateofbirth)

    def set_address(self,address):
        self.driver.find_element_by_xpath(self.xpath_address_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_address_input_box).send_keys(address)

    def set_city(self,city):
        self.driver.find_element_by_xpath(self.xpath_city_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_city_input_box).send_keys(city)

    def set_state(self,state):
        self.driver.find_element_by_xpath(self.xpath_state_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_state_input_box).send_keys(state)

    def set_PIN_number(self,pinno):
        self.driver.find_element_by_xpath(self.xpath_pin_no_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_pin_no_input_box).send_keys(pinno)

    def set_mobile_number(self,mobile_number):
        self.driver.find_element_by_xpath(self.xpath_mobile_number_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_mobile_number_input_box).send_keys(mobile_number)

    def set_email_id(self,emailid):
        self.driver.find_element_by_xpath(self.xpath_email_id_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_email_id_input_box).send_keys(emailid)

    def set_password(self,password):
        self.driver.find_element_by_xpath(self.xpath_password_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_password_input_box).send_keys(password)

    def click_on_submit_button(self):
        self.driver.find_element_by_xpath(self.xpath_submit_button).click()

    def click_on_reset_button(self):
        self.driver.find_element_by_xpath(self.xpath_reset_button).click()