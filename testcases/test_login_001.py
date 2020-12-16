import time
import pytest
from utilities.custom_logger import LogGen
from utilities.readProperties import ReadConfig
from pageobjects.login_page import LoginPage

class Test_Login_001:

    base_url=ReadConfig.get_base_URL()
    user_name=ReadConfig.get_user_name()
    password=ReadConfig.get_password()
    log=LogGen.log_gen()

    @pytest.mark.smoke
    def test_open_browser(self,setup):
        self.log.info("------Open browser test------")
        self.driver=setup
        self.driver.get(self.base_url)
        actual_url=self.driver.current_url
        if actual_url=="http://demo.guru99.com/V4/":
            assert True
            self.log.info("------ open browser test passed ------")
            self.driver.close()
        else:
            self.driver.save_screenshot("../screenshots/"+'test_homepage_title.png')
            self.driver.close()
            self.log.error("------ open browser test failed ------")
            assert False

    @pytest.mark.smoke
    def test_home_page_title(self,setup):
        self.log.info("------ test login 001 -------")
        self.log.info("------ verifying homepage title ------")
        self.driver=setup
        self.driver.get(self.base_url)
        time.sleep(5)
        actual_title=self.driver.title
        if actual_title == "Guru99 Bank Home Page":
            assert True
            self.driver.close()
            self.log.info("------ home page title test is passed ------")
        else:
            self.driver.save_screenshot("../screenshots/"+'test_homepage_title.png')
            self.driver.close()
            self.log.error("------ home page title test is failed ------")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.log.info("------ verifyin login test ------")
        self.driver=setup
        self.driver.get(self.base_url)
        self.log.info("--- application launched...")
        self.lp=LoginPage(self.driver)
        self.lp.set_user_id(self.user_name)
        self.log.info("--- user id Entered : "+self.user_name)
        self.lp.set_password(self.password)
        self.log.info("--- password Entered : "+self.password)
        self.lp.click_on_login()
        self.log.info("--- clicked on login")
        self.msg=self.driver.find_element_by_xpath("//body").text

        #if self.msg == "Manger Id : mngr285385":
        if "Manger Id :"+" "+self.user_name in self.msg:
            assert True
            self.log.info("------ login test is passed ------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.log.error("------ login test is failed")
            assert False
