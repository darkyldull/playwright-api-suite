import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title(re.compile("Swag"))

def test_can_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name = "Username").fill("standard_user")
    page.get_by_role("textbox", name = "Password").fill("secret_sauce")
    page.get_by_text("Login").click() 

    expect(page.get_by_text("Products")).to_be_visible()


def test_can_not_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_role("textbox", name = "Username").fill("standard_user")
    page.get_by_role("textbox", name = "Password").fill("secret_sauced")
    page.get_by_text("Login").click() 

    expect(page.get_by_text("Epic sadface")).to_be_visible()

def test_add_to_cart(logged_in_page: Page):

    logged_in_page.get_by_text("Add to cart").first.click()
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("1")

def test_checkout(logged_in_page: Page):


    logged_in_page.get_by_text("Add to cart").first.click()
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("1")

    cart_badge.click()

    logged_in_page.get_by_text("Checkout").click()

    logged_in_page.get_by_role("textbox", name = "First Name").fill("John")
    logged_in_page.get_by_role("textbox", name = "Last Name").fill("Doe")
    logged_in_page.get_by_role("textbox", name = "Zip/Postal Code").fill("123456")
    logged_in_page.get_by_text("Continue").click()

    logged_in_page.get_by_text("Finish").click()

    expect(logged_in_page.get_by_text("Thank you for your order!")).to_be_visible()