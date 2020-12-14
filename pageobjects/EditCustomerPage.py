


class EditCustomerPage:

    link_text_edit_customer_link="Edit Customer"
    xpath_custmer_id_input_box="//input[@name='cusid']"
    xpath_submit_button_page1="//input[@name='AccSubmit']"
    xpath_reset_button_page1="//input[@name='res']"
    #Edit Customer page Locaters after Entering Cust ID
    xpath_address_input_box="//textarea[@name='addr']"
    xpath_city_input_box="//input[@name='city']"
    xpath_state_input_box="//input[@name='state']"
    xpath_pin_no_input_box="//input[@name='pinno']"
    xpath_mobile_number_input_box="//input[@name='telephoneno']"
    xpath_email_id_input_box="//input[@name='emailid']"
    xpath_submit_button_page2="//input[@value='Submit']"
    xpath_reset_button_page2="//input[@value='Reset']"

    def __init__(self,driver):

        self.driver=driver
        self.driver.implicitly_wait(10)

    def click_on_edit_customer_link(self):
        self.driver.find_element_by_link_text(self.link_text_edit_customer_link).click()

    def set_customer_id(self,custid):
        self.driver.find_element_by_xpath(self.xpath_custmer_id_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_custmer_id_input_box).send_keys(custid)

    def click_on_Page_1_submit_button(self):
        self.driver.find_element_by_xpath(self.xpath_submit_button_page1).click()

    def click_on_page_1_reset_button(self):
        self.driver.find_element_by_xpath(self.xpath_reset_button_page1).click()

    def set_address(self,address):
        self.driver.find_element_by_xpath(self.xpath_address_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_address_input_box).send_keys(address)

    def set_city(self,city):
        self.driver.find_element_by_xpath(self.xpath_city_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_city_input_box).send_keys(city)

    def set_state(self,state):
        self.driver.find_element_by_xpath(self.xpath_state_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_state_input_box).send_keys(state)

    def set_pin_no(self,pinno):
        self.driver.find_element_by_xpath(self.xpath_pin_no_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_pin_no_input_box).send_keys(pinno)

    def set_mobile_number(self,mnumber):
        self.driver.find_element_by_xpath(self.xpath_mobile_number_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_mobile_number_input_box).send_keys(mnumber)

    def set_email_id(self,emailid):
        self.driver.find_element_by_xpath(self.xpath_email_id_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_email_id_input_box).send_keys(emailid)

    def click_on_page_2_submit_button(self):
        self.driver.find_element_by_xpath(self.xpath_submit_button_page2).click()

    def click_on_page_2_reset_button(self):
        self.driver.find_element_by_xpath(self.xpath_reset_button_page2).click()