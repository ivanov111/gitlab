import pytest
from selenium import webdriver
from contacts_page import ContactsPage
from about_page import AboutPage
from work_page import WorkPage


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestTensorWebsite:

    def test_tensor_website(self, driver):
        contacts_page = ContactsPage(driver)
        contacts_page.go_to_tensor()

        about_page = AboutPage(driver)
        about_page.open_about_page()

        work_page = WorkPage(driver)
        work_page.check_photo_sizes()
