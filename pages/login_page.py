from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):


    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTR_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTR).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTR_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_LINK).click()



    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "word \"login\" not in url"
        # assert self.browser.current_url, 'URL не корректный'


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.EMAIL_LINK), 'EMAIL link is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTR_LINK), 'EMAIL Registr link is not presented'