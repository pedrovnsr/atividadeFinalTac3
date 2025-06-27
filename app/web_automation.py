

from selenium.webdriver.common.by import By
from playwright.sync_api import expect

BASE_URL = "https://dummy.restapiexample.com/"

def get_title_and_screenshot(driver):
    driver.get(BASE_URL)
    saved = driver.save_screenshot("dummy-restapi-screenshot-1.png")
    if saved:
        return driver.title
    else:
        raise Exception("Não foi possível capturar Screenshot da página")

def get_title_and_screenshot_playwright(page):
    page.goto(BASE_URL)
    page.screenshot(path="dummy-restapi-screenshot-2.png", full_page=True)

def get_table_columns(driver):
    driver.get(BASE_URL)
    driver.implicitly_wait(0.5)
    table = driver.find_element(By.TAG_NAME, "table")
    if table:
        # Obtém todos os elementos com tag th (cabeçalho)
        colunas = table.find_elements(by=By.CSS_SELECTOR, value="thead th")
        return [ col.text for col in colunas if col.text != "#"]
    else:
        raise Exception("Não foi possível encontrar uma tabela na página")
    
def get_table_columns_playwright(page):
    page.goto(BASE_URL)
    expect(page.locator("table")).to_be_visible()
    # Cria localizador com todos os elementos com tag th (cabeçalho) filtra o cabeçalho com texto "#"
    return page.locator("table thead th").filter(has_not_text="#")
