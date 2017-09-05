from address_book.book.processors.processor import Processor


class GroupProcessor(Processor):
    @property
    def collection(self):
        return self.book.groups

    def add(self, group):
        self.collection.add(group)
        for person in group.persons:
            person.groups.add(group)
            if person not in self.book:
                self.book.add(person)

    def discard(self, group):
        self.collection.discard(group)
        for person in group.persons:
            person.groups.discard(group)
