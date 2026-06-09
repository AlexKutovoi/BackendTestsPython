import allure
from playwright.sync_api import Page

from src.main.ui.pages.login_page import LoginPage
from utils.constants import Urls


class LoginSteps:
    LOGIN_URL = Urls.BASE

    def __init__(self, page:Page):
        self.page = page
        self.login_page = LoginPage(self.page)

    @allure.step('Open login page')
    def open_login_page(self):
        self.login_page.open()
        return self

    @allure.step('Login user {username}')
    def login(self, username: str, password: str):
        self.login_page.login(username, password)
        return self

    @allure.step('Get error message login')
    def get_error_text(self) -> str:
        return self.login_page.get_error()
