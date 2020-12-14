import configparser

config=configparser.RawConfigParser()
config.read("./configuration/config.ini")

class ReadConfig:

    @staticmethod
    def get_base_URL():
        url=config.get("Version_4","base_url")
        return url

    @staticmethod
    def get_user_name():
        user_name=config.get("Version_4","user_name")
        return user_name

    @staticmethod
    def get_password():
        password=config.get("Version_4","password")
        return password

