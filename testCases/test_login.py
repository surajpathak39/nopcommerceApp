import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    baseURL = ReadConfig.getApplicationURL()
    # useremail = "admin@yourstore.com"
    useremail = ReadConfig.getUseremail()
    # password = "admin"
    password = ReadConfig.getUserPassword()
    logger = LogGen.getLogger()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        # path = "C:\\Users\\durap\\Downloads\\chromedriver\\chromedriver.exe"
        # service_obj = Service(executable_path=path)
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.logger.info("*************** Test_001_Login ***************")
        # print(self.logger)
        self.logger.info("*************** Verify Home Page Title***************")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)

        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** Home Page Test is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()

            self.logger.error("*************** Home Page Test is failed***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Verifying Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************** Login Test Test is passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*************** Login Test is failed***************")
            assert False


