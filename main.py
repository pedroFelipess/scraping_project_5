import pandas as pd
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_EXEC = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if chrome_options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_sevice = Service(
        executable_path=str(CHROME_DRIVER_EXEC)
    )

    browser = webdriver.Chrome(
        service=chrome_sevice,
        options=chrome_options,
    )

    return browser


options = ()

name_products = []
price_products = []

i = 1

while True:
    browser = make_chrome_browser(*options)

    browser.get(f'https://www.pichau.com.br/monitores?page={i}')

    cards = browser.find_elements(By.CLASS_NAME, 'MuiCardContent-root')

    try:
        for card in cards:
            name_product = card.find_element(By.TAG_NAME, 'h2')

            price_layer_1 = card.find_element(By.TAG_NAME, 'div')
            price_layer_2 = price_layer_1.find_element(By.TAG_NAME, 'div')
            price_layer_3 = price_layer_2.find_element(By.TAG_NAME, 'div')
            price_product = price_layer_3.find_elements(By.TAG_NAME, 'div')

            if len(price_product) != 2:
                name_products.append(name_product.text)
                price_products.append(price_product[0].text)
                continue

            name_products.append(name_product.text)
            price_products.append(price_product[1].text)
    except Exception:
        print('Process completed.')
        break

    browser.close()

    i += 1

infos = {'Name': name_products, 'Price': price_products}
df = pd.DataFrame(infos)
df.to_csv('pichau_monitors.csv', encoding='utf8', index=False)
