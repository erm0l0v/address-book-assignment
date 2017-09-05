from address_book.models import Model


class Person(Model):

    def __init__(self, first_name, last_name, street_addresses=None, emails=None, phone_numbers=None, groups=None):
        self.first_name = first_name
        self.last_name = last_name
        self.street_addresses = street_addresses or set()
        self.emails = emails or set()
        self.phone_numbers = phone_numbers or set()
        self.groups = groups or set()

    @property
    def key(self):
        return self.first_name, self.last_name
