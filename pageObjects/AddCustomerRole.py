from selenium.webdriver.common.by import By
import time


class AddCustomerRole:
    linkCustomer_Role_menuItem_xpath = "//a[@href='/Admin/CustomerRole/List']"
    btn_add_newCustomer_role_xpath = "//a[@class='btn btn-primary']"
    text_name_id = "Name"
    checkbox_freeshipping_id = "FreeShipping"
    button_popupwindow_choose_a_product_xpath = "//button[normalize-space()='Choose a product']"
    btnSelect_xpath = "//tbody/tr[1]/td[1]/button[1]"
    text_systemName_id = "SystemName"
    btn_save_xpath = "//button[@name='save']"
    success_message_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerRoleMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_Role_menuItem_xpath).click()

    def clickOnAddNewCustBtn(self):
        self.driver.find_element(By.XPATH, self.btn_add_newCustomer_role_xpath).click()

    def setCustomerName(self, Name_text):
        self.driver.find_element(By.ID, self.text_name_id).clear()
        self.driver.find_element(By.ID, self.text_name_id).send_keys(Name_text)

    def setSystemName(self, SystemName):
        self.driver.find_element(By.ID, self.text_systemName_id).clear()
        self.driver.find_element(By.ID, self.text_systemName_id).send_keys(SystemName)

    def newWindowPopUp(self):
        main_page = self.driver.current_window_handle
        self.driver.find_element(By.XPATH, self.button_popupwindow_choose_a_product_xpath).click()

        # self.addcustrole.newWindowPurchaseProduct()
        for handle in self.driver.window_handles:
            if handle != main_page:
                pop_page = handle
        time.sleep(5)
        self.driver.switch_to.window(pop_page)
        self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/button[1]").click()
        self.driver.switch_to.window(main_page)
        txt = self.driver.find_element(By.XPATH, "//span[@id='purchased-with-product-name']").text
        return txt

    def selectProduct(self):
        self.driver.find_element(By.XPATH, self.btnSelect_xpath).click()

    def clickSavebutton(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def getsuccessMsg_AddedRole(self):
        return self.driver.find_element(By.XPATH, self.success_message_xpath).text
