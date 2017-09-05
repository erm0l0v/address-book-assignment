from address_book.book.processors.processor import Processor
from address_book.book import indexes


class PersonProcessor(Processor):
    index_classes = [
        indexes.PersonNameIndex,
        indexes.PersonEmailIndex
    ]

    @property
    def collection(self):
        return self.book.persons

    def add(self, person):
        self.collection.add(person)
        for group in person.groups:
            group.persons.add(person)
            if group not in self.book:
                self.book.add(group)

    def discard(self, person):
        self.collection.discard(person)
        for group in person.groups:
            group.persons.discard(person)
            if not group.persons and group in self.book:
                self.book.discard(group)
