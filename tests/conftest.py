import pytest
from selenium import webdriver
from src.utilities.loggers import get_logger
from src.config.config import  config

import os
logger = get_logger(__name__)


def pytest_runtest_setup(item):

    logger.info(f"\n{'=' * 80}")
    logger.info(f"TEST START: {item.name}")
    logger.info(f"{'=' * 80}")


def pytest_runtest_teardown(item, nextitem):

    logger.info(f"{'=' * 80}")
    logger.info(f"TEST END: {item.name}")
    logger.info(f"{'=' * 80}\n")

def pytest_runtest_makereport(item, call):

    if call.excinfo is not None:
        logger.error(f"Γ£ù Test Failed: {item.name}")
        logger.error(f"Error: {call.excinfo.value}")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser",default=config.get_browser)
    print(browser)
    driver=webdriver.Chrome()
    print("Session Started")
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    from src.utilities.helpers import FileReader

    logger.info("Loading test data")
    test_data_file = os.path.join("test_data", "test_data.json")

    return FileReader.read_json(test_data_file)

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Select browser")
