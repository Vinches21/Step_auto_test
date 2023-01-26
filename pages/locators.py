from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

class LoginPageLocators():
    EMAIL_LINK = (By.XPATH, '//input[@name="login-username"]')
    EMAIL_REGISTR_LINK = (By.XPATH, '//input[@name="registration-email"]')

class ProductLocators():
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_NAME_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRICE_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')






