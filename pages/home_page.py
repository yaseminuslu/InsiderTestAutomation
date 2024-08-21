import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            cookie_button.click()
        except Exception as e:
            print("Çerez uyarısı bulunamadı veya kapatılamadı:", e)

    def go_to_careers_page(self):
        company_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[2]/div/ul[1]/li[6]/a"))
        )
        company_menu.click()

        careers_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Careers"))
        )
        time.sleep(2)
        careers_link.click()
