import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope="class")
# def driver():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.maximize_window()
#     yield driver
#     driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
