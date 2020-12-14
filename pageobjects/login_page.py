from utilities.seleniumbase import SeleniumBase

class LoginPage:
    name_user_id = "uid"
    name_password = "password"
    name_login_button = "btnLogin"
    linktext_logout_link = "Log out"
    expected_title = "Guru99 Bank Manager HomePage"

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    def set_user_id(self,user_name):
        self.driver.find_element_by_name(self.name_user_id).clear()
        self.driver.find_element_by_name(self.name_user_id).send_keys(user_name)

    def set_password(self,password):
        self.driver.find_element_by_name(self.name_password).clear()
        self.driver.find_element_by_name(self.name_password).send_keys(password)

    def click_on_login(self):
        self.driver.find_element_by_name(self.name_login_button).click()

    def click_on_logout(self):
        self.driver.find_element_by_link_text(self.linktext_logout_link).click()


