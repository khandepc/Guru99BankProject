


class DeleteCustomerPage:

    link_text_delete_customer_link="Delete Customer"
    xpath_customer_id_input_box="//input[@name='cusid']"
    xpath_submit_button="//input[@name='AccSubmit']"
    xpath_reset_button="//input[@name='res']"


    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    def click_on_delete_customer_link(self):
        self.driver.find_element_by_link_text(self.link_text_delete_customer_link)

    def set_customer_id(self,custid):
        self.driver.find_element_by_xpath(self.xpath_customer_id_input_box).clear()
        self.driver.find_element_by_xpath(self.xpath_customer_id_input_box).send_keys(custid)

    def click_on_submit_button(self):
        self.driver.find_element_by_xpath(self.xpath_submit_button).click()

    def click_on_reset_button(self):
        self.driver.find_element_by_xpath(self.xpath_reset_button).click()

