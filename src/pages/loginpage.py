from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "enterimg")


    def __init__(self,driver):
        super().__init__(driver)

    def get_url(self,url):
        self.goto_url(url)

    def enter_username(self,username):
        self.send_text(self.USERNAME_INPUT,username)

    def enter_password(self,password):
        self.send_text(self.PASSWORD_INPUT,password)
    def click_login(self):
        self.click_button(self.LOGIN_BUTTON)

