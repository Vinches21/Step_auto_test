from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

class LoginPageLocators():
    EMAIL_LINK = (By.XPATH, '//input[@name="login-username"]')
    EMAIL_REGISTR_LINK = (By.XPATH, '//input[@name="registration-email"]')
    PASSWORD_REGISTR = (By.XPATH, '//input[@name="registration-password1"]')
    PASSWORD_REGISTR_2 = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_LINK = (By.XPATH, '//button[@name="registration_submit"]')

class ProductLocators():
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    BOOK_NAME_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRICE_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')

class BasketLocators():
    BASKET = (By.XPATH, '//a[@class="btn btn-default"]')
    MESSAGE_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    MESSAGE_PRODUCTS_IN_BASKET = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')







