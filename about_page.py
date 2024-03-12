from selenium.webdriver.common.by import By
from pageobject import PageObject


class AboutPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)

    def open_about_page(self):
        strength_in_people = self.find_element((By.XPATH, "//*[contains(text(), 'Сила в людях')]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", strength_in_people)
        learn_more = self.find_element((By.XPATH, "//a[@href='/about']"))
        learn_more.click()
