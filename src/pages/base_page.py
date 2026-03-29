from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()
        self.wait=WebDriverWait(driver,10)
    def goto_url(self,url):
        self.driver.get(url)
    def click_button(self,element):
        self.wait.until(EC.element_to_be_clickable(element)).click()
    def send_text(self,element,text):
        self.wait.until(EC.presence_of_element_located(element)).send_keys(text)

