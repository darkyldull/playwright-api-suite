import pytest
from playwright.sync_api import Page

@pytest.fixture
def logged_in_page(page: Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name = "Username").fill("standard_user")
    page.get_by_role("textbox", name = "Password").fill("secret_sauce")
    page.get_by_text("Login").click() 
    
    return page