from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class QAJobsPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_jobs_list(self):

        jobs_list_container = self.driver.find_element(By.XPATH, "//*[@id='jobs-list']")

        self.driver.execute_script("""
            var element = arguments[0];
            var rect = element.getBoundingClientRect();
            var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            var elementCenter = rect.top + scrollTop + rect.height / 2 - window.innerHeight / 2;
            window.scrollTo({
                top: elementCenter,
                behavior: 'smooth'
            });
        """, jobs_list_container)
        time.sleep(2)

    def get_job_listings(self):
        self.scroll_to_jobs_list()
        job_list_elements = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='jobs-list']//div[contains(@class, 'position-list-item-wrapper')]")
            )
        )
        return job_list_elements

    def click_view_role(self, job):
        view_role_button = job.find_element(By.XPATH, ".//a[contains(text(), 'View Role')]")
        view_role_button.click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)

        assert "lever.co" in self.driver.current_url, "Başvuru Sayfasına Yönlendirme Başarısız."
        print("Başvuru sayfasına Yönlendirme Başarılı.")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])