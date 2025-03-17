from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, ttk

INITIAL_PRICE = 100.00
URL = 'https://www.finam.ru/quote/batsnq/aapl/'

with webdriver.Chrome() as browser:
    browser.get(URL)
    price_text = WebDriverWait(browser, 200).until(
        EC.visibility_of_element_located((By.ID, "finfin-local-plugin-quote-item-review-price"))
    ).text

price = float(price_text.replace("$", "").replace(",", "."))

if price - INITIAL_PRICE >= 5.00:
    root = Tk()
    ttk.Label(root, text=f"Current price: {price}, difference: {price - INITIAL_PRICE}").pack(padx=10, pady=10)
    root.mainloop()
