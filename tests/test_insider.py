import unittest
from selenium.webdriver.common.by import By
from pages.browser_setup import setup_browser
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

class TestInsider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = setup_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_insider(self):
        driver = self.driver
        driver.get("https://useinsider.com/")
        self.assertIn("#1 Leader in Individualized, Cross-Channel CX — Insider", driver.title)
        print("Ana sayfa doğrulandı.")

        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.go_to_careers_page()
        self.assertIn("Insider Careers", driver.title)
        print("Career sayfası doğrulandı.")

        careers_page = CareersPage(driver)
        elements_to_scroll_and_check = [
            ("See all teams", By.XPATH, "//a[contains(text(), 'See all teams')]"),
            ("Life at Insider", By.XPATH, "//h2[contains(text(), 'Life at Insider')]"),
            ("Our Locations", By.XPATH, "//h3[contains(text(), 'Our Locations')]")
        ]

        for text, by, locator in elements_to_scroll_and_check:
            careers_page.scroll_to_element(by, locator)
            careers_page.check_text_exists(text, by, locator)

        driver.get("https://useinsider.com/careers/quality-assurance/")
        self.assertIn("Insider quality assurance job opportunities", driver.title)
        print("Quality assurance sayfası doğrulandı.")

        careers_page.filter_jobs()
        qa_jobs_page = QAJobsPage(driver)

        job_list_elements = qa_jobs_page.get_job_listings()

        if job_list_elements:
            print("İş ilanları mevcut.")
            for job in job_list_elements:
                qa_jobs_page.click_view_role(job)
        else:
            print("İş ilanı bulunamadı.")

if __name__ == "__main__":
    unittest.main()