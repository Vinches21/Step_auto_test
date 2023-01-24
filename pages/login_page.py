from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        print('1')
        self.should_be_login_form()
        print('2')
        self.should_be_register_form()
        print('3')

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