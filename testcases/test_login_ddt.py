import time
import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import XLUties
from pageobjects.login_page import LoginPage


class TestLoginDDT_001:

    baseURL=ReadConfig.get_base_URL()
    logger=LogGen.log_gen()
    Datapath="./testdata/TestDataManagerLogin.xlsx"

    def test_login_ddt(self,setup):
        self.logger.info("****** TestLoginDDT_001 started ******")
        self.logger.info("****** verifying login ddt test ******")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.rows=XLUties.get_row_count(self.Datapath,"Sheet1")
        print("Number of rows in Excel Data ",self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.username=XLUties.read_data(self.Datapath,"Sheet1",r,1)
            self.password=XLUties.read_data(self.Datapath,"Sheet1",r,2)
            self.exp=XLUties.read_data(self.Datapath, "Sheet1",r,3)

            self.lp.set_user_id(self.username)
            self.lp.set_password(self.password)
            self.lp.click_on_login()
            actual_title=self.driver.title
            expected_title="Guru99 Bank Manager HomePage"
            if actual_title==expected_title:
                if self.exp=="Pass":
                    self.logger.info("------Passed------")
                    self.lp.click_on_logout()
                    self.driver.switch_to.alert.accept()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("------Failed------")
                    self.lp.click_on_logout()
                    time.sleep(5)
                    self.driver.switch_to.alertaccept()
                    lst_status.append("Fail")
            elif actual_title!=expected_title:
                if self.exp=="Pass":
                    self.logger.info("------Failed------")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("------Passed------")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("****** TestLoginDDT_001 Passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** TestLoginDDT_001 Failed ******")
            self.driver.close()
            assert False
        self.logger.info("****** End of login DDT test ******")
        self.logger.info("**************** complete test login DDT ********************")
