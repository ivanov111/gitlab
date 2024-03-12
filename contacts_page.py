from selenium.webdriver.common.by import By
from pageobject import PageObject


class ContactsPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_tensor(self):
        self.driver.get("https://sbis.ru/")
        self.find_element((By.LINK_TEXT, "Контакты")).click()
        tensor_banner = self.find_element((By.CSS_SELECTOR, "a[href='https://tensor.ru/']"))
        tensor_banner.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
