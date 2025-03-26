import time

import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class seleniumBaseSwagLabs():

    def selenium_init(self):
        print("start test")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()

        driver.implicitly_wait(20)
        self.driver=driver
        return driver

    def selenium_end(self,driver):
        self.driver.close()
        print("test end")
        print("cosmetic change")




