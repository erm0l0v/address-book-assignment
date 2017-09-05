from collections import MutableSet
from itertools import chain

from address_book.book import tools, indexes


class Book(MutableSet):
    def __init__(self):
        self.persons = set()
        self.groups = set()
        self.index_storage = dict()
        self.indexes = [
            indexes.PersonNameIndex(self),
            indexes.PersonEmailIndex(self)
        ]

    def __contains__(self, x):
        processor = tools.get_processor(self, x)
        return x in processor.collection

    def add(self, value):
        processor = tools.get_processor(self, value)
        result = processor.add(value)
        update_indexes = [ind for ind in self.indexes if type(ind) in processor.index_classes]
        for index in update_indexes:
            index.add_value(value)
        return result

    def __len__(self):
        return len(self.persons) + len(self.groups)

    def discard(self, value):
        processor = tools.get_processor(self, value)
        result = processor.discard(value)
        update_index = [ind for ind in self.indexes if type(ind) in processor.index_classes]
        for index in update_index:
            index.remove(value)
        return result

    def __iter__(self):
        return chain(self.persons, self.groups)
