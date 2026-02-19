class Book:
    _stars_to_number = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }
    def __init__(self, title, price, rating):
        self.title = title
        self.price = price
        self.rating = rating
        self.rating_int = self._stars_to_number[rating]


    def __str__(self):
        return f"Book:\t{self.price}\t\t{self.title}\t{'⭐' * self.rating_int}"

    def to_dict(self):
        return {'Title':self.title, 'Price':self.price, 'Rating':self.rating}
