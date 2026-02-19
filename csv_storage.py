import csv
import os
from datetime import datetime
from pathlib import Path

from book import Book

WORKDIR = Path(__file__).resolve().parent
DATADIR = WORKDIR / 'data'


class CSVStorage:
    @staticmethod
    def save(books: list[Book], filename: str = 'books_data'):
        os.makedirs(DATADIR, exist_ok=True)
        filename = f"{filename}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        with open(DATADIR / filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, ['Title', 'Price', 'Rating'])
            writer.writerows(map(lambda b: b.to_dict(), books))