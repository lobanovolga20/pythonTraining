from selenium.webdriver.common.by import By


class productPage():

    def __init__(self,driver):   #initiationg the product page
        self.driver=driver


    def get_first_price(self):
        first_price=self.driver.find_element(By.CLASS_NAME,"inventory_item_price")
        first_price_text=first_price.text
        assert first_price_text=="$29.99","First price is not as expected"  #after the comma, will show the message if the condition in assert is not happening


