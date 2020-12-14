import time
import pytest
from utilities.custom_logger import LogGen
from utilities.readProperties import ReadConfig
from pageobjects.login_page import LoginPage


class TestCustomerModule:

    baseURL=ReadConfig.get_base_URL()
    user_name=ReadConfig.get_user_name()
    password=ReadConfig.get_password()


