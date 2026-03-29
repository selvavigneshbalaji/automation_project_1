import pytest

from src.pages.loginpage import LoginPage
from src.config import config
from src.utilities.loggers import get_logger

logger =get_logger(__name__)
def test_login(setup):
    logger.info("Starting the application")
    driver=setup
    logger.info("Setting up page")
    print(config.base_url)
    login_page=LoginPage(driver)
    login_page.get_url(config.base_url)
    login_page.enter_username("demousername")
    login_page.click_login()
    logger.info("Login Succesfully")

@pytest.mark.smoke
def test_login_with_data(setup,test_data):
    logger.info("Starting the application")
    driver=setup
    login_page=LoginPage(driver)
    login_page.get_url(config.base_url)
    user=test_data["valid_users"][0]
    username=user["username"]
    login_page.enter_username(username)
    login_page.click_login()
    logger.info("Login Succesfully")



