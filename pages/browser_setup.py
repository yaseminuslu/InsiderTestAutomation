import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver