from src.pages.base_page import  BasePage
from selenium.webdriver.common.by import By


class Switch(BasePage):
    switch_dropdowm=(By.XPATH,"//a[@href='SwitchTo.html' and text()='SwitchTo']")
    switch_to_frames=(By.XPATH,"//a[@href='Frames.html' and text()='Frames']")
    switch_to_singleiframe=(By.XPATH,"//a[@href='#Single' and text()='Single Iframe ']")
    enter_text_in_singleiframe=(By.XPATH,"//iframe[@id='singleframe']")
    switch_to_multiple_frame=(By.XPATH,"//a[@href='#Multiple' and text()='Iframe with in an Iframe']")
    iframe_multiple=(By.XPATH,"//iframe[@src='MultipleFrames.html']")
    iframe_single = (By.XPATH, "//iframe[@src='SingleFrame.html']")
    enter_text_iframe=(By.XPATH,"//input[@type='text']")



    def __init__(self, driver):
        super().__init__(driver)
    def click_switch_dropdown(self):
        self.click_button(self.switch_dropdowm)
        self.click_button(self.switch_to_frames)

    def enter_text_in_single(self, text):
        self.switch_to_frame(self.enter_text_in_singleiframe)
        self.send_text(self.enter_text_iframe,text)
        self.switch_to_default_content()


    def enter_text_in_multiple(self,text):
        self.click_button(self.switch_to_multiple_frame)
        self.switch_to_frame(self.iframe_multiple)
        self.switch_to_frame(self.iframe_single)
        self.send_text(self.enter_text_iframe, text)
        self.switch_to_default_content()


