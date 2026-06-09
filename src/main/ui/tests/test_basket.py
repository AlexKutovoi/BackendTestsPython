from steps.basket_steps import BasketSteps
from steps.catalog_steps import CatalogSteps
from steps.checkout_steps import CheckoutSteps

def test_add_item_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    catalog.add_to_cart('Sauce Labs Backpack')
    basket.open_cart()
    basket.expect_item_in_cart('Sauce Labs Backpack')

def test_add_two_item_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    catalog.add_to_cart('Sauce Labs Fleece Jacket')
    catalog.add_to_cart('Sauce Labs Bolt T-Shirt')
    basket.open_cart()
    basket.expect_item_in_cart('Sauce Labs Fleece Jacket')
    basket.expect_item_in_cart('Sauce Labs Bolt T-Shirt')

def test_remove_item_from_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    catalog.add_to_cart('Sauce Labs Fleece Jacket')
    basket.open_cart()
    basket.expect_item_in_cart('Sauce Labs Fleece Jacket')
    basket.remove_item('Sauce Labs Fleece Jacket')
    basket.expect_item_not_in_cart('Sauce Labs Fleece Jacket')

def test_remove_items_from_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    catalog.add_to_cart('Sauce Labs Backpack')
    catalog.add_to_cart('Test.allTheThings() T-Shirt (Red)')
    basket.open_cart()
    basket.expect_item_in_cart('Sauce Labs Backpack')
    basket.expect_item_in_cart('Test.allTheThings() T-Shirt (Red)')
    basket.remove_item('Sauce Labs Backpack')
    basket.remove_item('Test.allTheThings() T-Shirt (Red)')
    basket.expect_item_not_in_cart('Sauce Labs Backpack')
    basket.expect_item_not_in_cart('Test.allTheThings() T-Shirt (Red)')

def test_checkout_multipe_items(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    catalog.add_to_cart('Sauce Labs Fleece Jacket')
    catalog.add_to_cart('Sauce Labs Bolt T-Shirt')
    basket.open_cart()
    basket.expect_item_in_cart('Sauce Labs Fleece Jacket')
    basket.expect_item_in_cart('Sauce Labs Bolt T-Shirt')
    basket_total = basket.get_items_total_price()
    basket.checkout()
    checkout.start_checkout(first_name='Max', last_name='Kim', postal_code='456333')
    checkout_total = checkout.get_item_total_after_continue()
    assert checkout_total == basket_total, 'Sum items in Checkout != sum in busket'


def test_checkout_without_items(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)
    catalog.login('standard_user', 'secret_sauce')
    basket.open_cart()
    items = basket.get_item_names()
    assert len(items) == 0, 'No items in basket'
    basket.checkout()
    checkout.start_checkout(first_name='Max', last_name='Kim', postal_code='')
    error_text = checkout.get_error_message()
    assert error_text != '', 'Wait error empty basket'
