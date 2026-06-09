import allure
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout = CheckoutPage(page)

    @allure.step('Checkout firts_name, last_name, postal_code')
    def start_checkout(self, first_name: str, last_name: str, postal_code: str):
        self.checkout.start_checkout(first_name, last_name, postal_code)
        return self
    @allure.step('End checkout')
    def finish_checkout(self):
        self.checkout.finish_checkout()
        return self
    @allure.step('Get error on checkout page')
    def get_error_message(self)-> str:
        return self.checkout.get_error_message()
    @allure.step('Get sum all products after continue')
    def get_item_total_after_continue(self)->float:
        return self.checkout.get_item_total_after_continue()