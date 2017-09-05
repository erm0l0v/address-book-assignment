from address_book import models
from address_book.book import processors


def get_processor(book, data):
    data_type = type(data)
    result = None
    if issubclass(data_type, models.Person):
        result = processors.PersonProcessor(book)
    elif issubclass(data_type, models.Group):
        result = processors.GroupProcessor(book)
    if result is None:
        raise TypeError("Not supported type {}".format(data_type))
    return result
