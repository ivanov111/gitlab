import time
from selenium.webdriver.common.by import By
from pageobject import PageObject


class WorkPage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)

    def check_photo_sizes(self):
        work = self.find_element((By.XPATH, "//h2[text()='Работаем']"))
        self.driver.execute_script("arguments[0].scrollIntoView();", work)
        time.sleep(2)
        photos = work.find_elements(By.TAG_NAME, "img")

        for photo in photos:
            assert photo.get_attribute("height") == photos[0].get_attribute("height")
            assert photo.get_attribute("width") == photos[0].get_attribute("width")
