from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageObject:

    def __init__(self, driver):
        self.driver = driver

    def go_to_tensor(self):
        self.driver.get("https://sbis.ru/")
        self.find_element((By.LINK_TEXT, "Контакты")).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )


