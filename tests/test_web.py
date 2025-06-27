
import re
import requests
from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect

from app.web_automation import (
    get_title_and_screenshot,
    get_title_and_screenshot_playwright,
    get_table_columns,
    get_table_columns_playwright)

# Test 7: Captura título da pagina e salva screenshot

def test_get_title_and_screenshot(driver):
    title = get_title_and_screenshot(driver)
    assert "Dummy sample" in title

def test_get_title_and_screenshot_playwright(page: Page):
    get_title_and_screenshot_playwright(page)
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Dummy sample"))


# Test 8: Verifica a presença de tabela no HTML com colunas específicas
def test_get_table_columns(driver):
    cols = get_table_columns(driver)
    assert cols == ["Route", "Method", "Type", "Full route", "Description", "Details"]

def test_get_table_columns_playwright(page: Page):
    locator = get_table_columns_playwright(page)
    expect(locator).to_have_text(["Route", "Method", "Type", "Full route", "Description", "Details"])
