from address_book.book import indexes


class Repository(object):

    def __init__(self, book):
        self.book = book

    def save(self, obj):
        self.book.add(obj)

    def find_persons_by_name(self, term):
        index = indexes.PersonNameIndex(self.book)
        return index.filter(term)

    def find_persons_by_email(self, term):
        index = indexes.PersonEmailIndex(self.book)
        return index.filter(term)
