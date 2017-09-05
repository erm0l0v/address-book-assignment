import string

import re

from address_book.book.indexes.base_index import BaseIndex


class PersonNameIndex(BaseIndex):
    name = 'person_name_index'

    def get_keys(self, value):
        names = [value.first_name, value.last_name]
        names = [self.get_keys_for_filter(n)[0] for n in names]
        names = list(filter(None, names))
        result = set(names)
        result.add(''.join(names))
        result.add(''.join(reversed(names)))
        return list(result)

    def get_keys_for_filter(self, term):
        translate_table = string.punctuation + string.whitespace + ' '
        formatted = re.sub('[{}]'.format(translate_table), '', term)
        return [formatted]
