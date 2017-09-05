import weakref
from collections import defaultdict


class BaseIndex(object):
    name = ''

    def __init__(self, book):
        self.book = book
        if not self.name:
            raise AttributeError('name is required')
        if self.name not in self.book.index_storage:
            self.book.index_storage.setdefault(self.name, defaultdict(weakref.WeakSet))

    @property
    def storage(self):
        return self.book.index_storage.get(self.name)

    def set_value(self, value, *keys):
        for key in keys:
            self.storage[key].add(value)

    def get_values(self, *keys):
        result = set()
        for key in keys:
            result |= set(self.storage.get(key, set()))
        return list(result)

    def remove_value(self, value, *keys):
        for key in keys:
            self.storage[key].discard(value)
            if len(self.storage[key]) == 0:
                del self.storage[key]

    def get_keys(self, value):
        raise NotImplementedError('Not implemented')

    def get_keys_for_filter(self, term):
        return [term]

    def filter(self, term):
        return self.get_values(*self.get_keys_for_filter(term))

    def add_value(self, value):
        keys = self.get_keys(value)
        self.set_value(value, *keys)

    def remove(self, value):
        keys = self.get_keys(value)
        self.remove_value(value, *keys)

    def refresh(self, value):
        self.remove(value)
        self.add_value(value)
