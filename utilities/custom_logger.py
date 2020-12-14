import logging
import inspect


class LogGen:

    @staticmethod
    def log_gen():
        #it will take test method name at run time
        logger_name=inspect.stack()[1][3]
        logger=logging.getLogger(logger_name)

        file_handler=logging.FileHandler("./logs/automation.log")

        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

        return logger