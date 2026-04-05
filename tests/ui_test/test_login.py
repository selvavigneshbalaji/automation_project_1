import pytest
import os
from src.pages.loginpage import LoginPage
from src.config import config
from src.utilities.loggers import get_logger
from src.pages.switch_class import Switch

logger = get_logger(__name__)


def test_login(setup):
    logger.info("Starting the application")
    driver = setup
    logger.info("Setting up page")
    print(config.base_url)
    login_page = LoginPage(driver)
    login_page.get_url(config.base_url)
    login_page.enter_username("demousername")
    login_page.click_login()
    logger.info("Login Succesfully")

def load_data():
    from src.utilities.helpers import FileReader

    logger.info("Loading test data")
    test_data_file = os.path.join("test_data", "test_data.json")

    return FileReader.read_json(test_data_file)
@pytest.mark.parametrize("test_d", load_data())
@pytest.mark.smoke
def test_login_with_data(setup, test_d):
    logger.info("Starting the application")
    driver = setup
    login_page = LoginPage(driver)
    login_page.get_url(config.base_url)
    user = test_d
    username = user["username"]
    login_page.enter_username(username)
    login_page.click_login()
    logger.info("Login Succesfully")


@pytest.mark.regression
def test_iframe(setup, test_data):
    logger.info("Starting the application")
    driver = setup
    login_page = LoginPage(driver)
    login_page.get_url(config.base_url)
    user = test_data["valid_users"][0]
    username = user["username"]
    login_page.enter_username(username)
    login_page.click_login()
    logger.info("Login Succesfully")
    test_iframes = Switch(driver)
    test_iframes.click_switch_dropdown()
    test_iframes.enter_text_in_single("test")
    test_iframes.enter_text_in_multiple("test2")
    logger.info("Close")
