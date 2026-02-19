from csv_storage import CSVStorage
from bookscraper import BookScraper

if __name__ == '__main__':
    scraper = BookScraper()
    books = scraper.scrape_books(pages=1)
    CSVStorage.save(books)
    print(f'Saved {len(books)} books!')