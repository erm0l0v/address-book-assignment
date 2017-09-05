from address_book.models.model import Model


class Group(Model):
    def __init__(self, name, persons=None):
        self.name = name
        self.persons = persons or set()

    @property
    def key(self):
        return self.name
