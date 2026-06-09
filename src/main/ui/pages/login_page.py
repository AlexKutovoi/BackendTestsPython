from playwright.sync_api import Page

from pages.base_pages import BasePage
from utils.constants import Urls


class LoginPage(BasePage):
    URL = Urls.BASE

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.error_message = page.locator('h3[data-test="error"]')

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error(self):
        return self.error_message.inner_text()

