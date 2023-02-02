import logging
import inspect


class LogGen:

    # def loggen(): logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s: %(levelname)s: %(
    # message)s', datefmt='%m/%d/%Y %I:%M:%S %p', encoding='utf-8', level=logging.INFO) logger = logging.getLogger()
    # logger.setLevel(logging.INFO) return logger
    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        # create log
        # logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(".\\Logs\\logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        # set level

        # logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger
