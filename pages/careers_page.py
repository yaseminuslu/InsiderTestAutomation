from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, by, locator):
        try:
            element = self.driver.find_element(by, locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            print(f"Sayfa '{locator}' elemanına kaydırıldı.")
        except:
            print(f"'{locator}' elemanına kaydırılamadı.")

    def check_text_exists(self, text, by, locator):
        try:
            self.driver.find_element(by, locator)
            print(f"'{text}' bulundu.")
        except:
            print(f"'{text}' bulunamadı.")

    def filter_jobs(self):
        wait = WebDriverWait(self.driver, 15)

        see_all_qa_jobs_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'See all QA jobs')]")))
        see_all_qa_jobs_button.click()
        time.sleep(5)

        department_select = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-filter-by-department-container"]')))
        department_select.click()

        try:
            quality_assurance_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//li[text()='Quality Assurance']")))
            quality_assurance_option.click()
        except Exception as e:
            print("Quality Assurance seçeneği bulunamadı veya tıklanamadı:", e)

        location_select = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-filter-by-location-container"]')))
        location_select.click()

        try:
            istanbul_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Istanbul, Turkey']")))
            istanbul_option.click()
        except Exception as e:
            print("İstanbul seçeneği bulunamadı veya tıklanamadı:", e)
        time.sleep(5)