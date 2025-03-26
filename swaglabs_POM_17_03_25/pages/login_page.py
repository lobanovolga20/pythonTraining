from selenium.webdriver.common.by import By

class loginPage():
    def __init__(self,driver):       #this is the constructor function
        self.driver=driver

    def set_user_and_pw(self,user_text,pw_text):
        user=self.driver.find_element(By.ID,"user-name")
        pw=self.driver.find_element(By.ID, "password")
        user.send_keys(user_text)
        pw.send_keys(pw_text)

    def click_on_login(self):
        login=self.driver.find_element(By.ID, "login-button")
        login.click()

