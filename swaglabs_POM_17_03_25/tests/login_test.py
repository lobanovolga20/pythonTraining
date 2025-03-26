import time

from swaglabs_POM_17_03_25.pages.login_page import loginPage
from swaglabs_POM_17_03_25.tests.product_test import productPage
from swaglabs_POM_17_03_25.tests.selenium_base_swag_labs import seleniumBaseSwagLabs


def test_correct_login_test():
    base=seleniumBaseSwagLabs()
    driver=base.selenium_init()
    login_page=loginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.set_user_and_pw("standard_user","secret_sauce")
    login_page.click_on_login()
    current_url=driver.current_url
    assert current_url=="https://www.saucedemo.com/inventory.html", "current URl is not as expected"

    base.selenium_end(driver)  #should be in the end of each function
time.sleep(5)

def test_incorrect_login_test():
    base = seleniumBaseSwagLabs()
    driver = base.selenium_init()
    login_page = loginPage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.set_user_and_pw("standard_user_fake", "secret_sauce")
    login_page.click_on_login()
    current_url = driver.current_url
    assert current_url == "https://www.saucedemo.com/", "current URl is not as expected"

    base.selenium_end(driver)
time.sleep(5)
def test_first_product():
        base = seleniumBaseSwagLabs()
        driver = base.selenium_init()
        login_page = loginPage(driver)
        product_page=productPage(driver)  #instance of the class
        driver.get("https://www.saucedemo.com/")
        login_page.set_user_and_pw("standard_user", "secret_sauce")
        login_page.click_on_login()
        product_page.get_first_price()

        base.selenium_end(driver)