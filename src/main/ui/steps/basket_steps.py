from playwright.sync_api import Page
import allure
from pages.basket_page import BasketPage


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket = BasketPage(page)

    @allure.step('Open basket')
    def open_cart(self):
        self.basket.open_cart()
        return self
    @allure.step('Check product in cart')
    def expect_item_in_cart(self, product_name: str):
        self.basket.expect_item_in_cart(product_name)
        return self

    @allure.step('Check product in cart')
    def expect_item_not_in_cart(self, product_name: str):
        self.basket.expect_item_not_in_cart(product_name)
        return self
    @allure.step('Remove item from cart')
    def remove_item(self, product_name: str):
        self.basket.remove_item(product_name)
        return self
    @allure.step('Go to checkout')
    def checkout(self):
        self.basket.checkout()
        return self
    @allure.step('Get list items name in cart')
    def get_item_names(self) -> list[str]:
        return self.basket.get_items_names()
    @allure.step('Get total price in cart')
    def get_items_total_price(self) -> float:
        return self.basket.get_items_total_price()
