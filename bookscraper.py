from typing import Optional

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from book import Book


class BookScraper:
    url = 'http://books.toscrape.com/'

    def __init__(self, timeout: int = 3):
        self.timeout: int = timeout
        self.driver: Optional[WebDriver] = None

    @staticmethod
    def _make_driver() -> WebDriver:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options)

        return driver

    def scrape_books(self, pages=50) -> list[Book]:
        if self.driver:
            self.driver.quit()
        self.driver = self._make_driver()
        books: list[Book] = []

        while True:
            pages -= 1
            page_books = self.scrape_page()
            books += page_books
            if not pages or not self._go_next_page():
                self.driver.quit()
                break
        return books

    def scrape_page(self) -> list[Book]:

        self.driver.get(self.url)

        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "li article.product_pod")
            ))

        books: list[Book] = []
        pods = self.driver.find_elements(By.CSS_SELECTOR, "li article.product_pod")

        for pod in pods:
            book = Book(
                title=pod.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title'),
                price=pod.find_element(By.CSS_SELECTOR, 'div p.price_color').text,
                rating=pod.find_element(By.CSS_SELECTOR, 'p.star-rating').get_attribute('class').split()[1]
            )
            books.append(book)
        return books

    def _go_next_page(self) -> bool:
        try:
            next_el = self.driver.find_element(By.CSS_SELECTOR, 'li.next a')
        except NoSuchElementException:
            print('No next page found')
            return False

        prev_url = self.driver.current_url

        next_el.click()

        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.current_url != prev_url)

        self.url = self.driver.current_url

        return True
