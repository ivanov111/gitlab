import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации драйвера."""
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


class SbisContactsPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть страницу контактов СБИС."""
        self.driver.get("https://sbis.ru/contacts")

    def wait_for_page_to_load(self):
        """Дождаться загрузки страницы."""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")))

    def get_region(self):
        """Получить текущий регион."""
        return self.driver.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text").text

    def click_on_region(self):
        """Кликнуть на кнопку выбора региона."""
        self.driver.find_element(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text").click()

    def wait_for_region_dropdown_to_open(self):
        """Дождаться открытия выпадающего списка регионов."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='sbis_ru-Region-Panel__list-l']")))

    def click_on_desired_region(self):
        """Кликнуть на нужный регион."""
        self.driver.find_element(By.XPATH, "//span[text()='41 Камчатский край']").click()

    def wait_for_region_to_be_selected(self):
        """Дождаться выбора региона."""
        time.sleep(2)

    def assert_selected_region(self):
        """Утвердить, что выбранный регион правильный."""
        assert self.driver.find_element(By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']").text == "Камчатский край"

    def assert_url_contains_region(self):
        """Утвердить, что URL содержит регион."""
        assert "41-kamchatskij-kraj" in self.driver.current_url

    def assert_title_contains_region(self):
        """Утвердить, что заголовок содержит регион."""
        assert "Камчатский край" in self.driver.title


def test_sbis_contacts_page(driver):
    """Тест страницы контактов СБИС."""
    page = SbisContactsPage(driver)
    page.open()
    page.wait_for_page_to_load()
    assert page.get_region() == "Ярославская обл."
    page.click_on_region()
    page.wait_for_region_dropdown_to_open()
    page.click_on_desired_region()
    page.wait_for_region_to_be_selected()
    page.assert_selected_region()
    page.assert_url_contains_region()
    page.assert_title_contains_region()
