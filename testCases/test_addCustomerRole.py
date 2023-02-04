import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.AddCustomerRole import AddCustomerRole
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_006_AddCustomerRole:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.getLogger()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomerRole(self, setup):
        self.logger.info("************* Test_006_AddCustomerRole **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Role Test **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()

        self.addcustrole = AddCustomerRole(self.driver)
        self.addcustrole.clickOnCustomerRoleMenuItem()
        self.addcustrole.clickOnAddNewCustBtn()
        self.logger.info("************* Providing customer role info **********")
        self.addcustrole.setCustomerName("TestRole")
        self.addcustrole.setSystemName("TestSystemName")
        self.txt = self.addcustrole.newWindowPopUp()
        print(self.txt)

        # main_page = self.driver.current_window_handle
        #
        # # self.addcustrole.newWindowPurchaseProduct()
        # for handle in self.driver.window_handles:
        #     if handle != main_page:
        #         pop_page = handle
        # time.sleep(5)
        # self.driver.switch_to.window(pop_page)
        # self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/button[1]").click()
        # self.driver.switch_to.window(main_page)
        # txt = self.driver.find_element(By.XPATH, "//span[@id='purchased-with-product-name']").text
        # self.logger.info("****************product is added*****************************")
        # time.sleep(5)
        # self.addcustrole.selectProduct()
        self.logger.info("****************product is added*****************************")
        self.addcustrole.clickSavebutton()

        self.logger.info("************* Saving customer_role info **********")
        self.logger.info("********* Add customer role validation started *****************")

        self.msgAddedRole = self.addcustrole.getsuccessMsg_AddedRole()
        if 'customer role has been added successfully.' in self.msgAddedRole:
            assert True
            self.logger.info("********* Add customer_role Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomerRole_scr.png")  # Screenshot
            self.logger.error("********* Add customer_role Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer role test **********")


# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))



