from address_book.book.indexes.base_index import BaseIndex

MIN_TERM_FOR_SEARCH_START = 1
MIN_TERM_FOR_SEARCH_CONTAINS = 3


def format_term(term):
    return term.strip().lower()


class PersonEmailIndex(BaseIndex):
    name = 'person_email_index'

    def get_keys(self, value):
        terms = filter(None, map(format_term, value.emails))
        return list(terms)

    def get_keys_for_filter(self, term):
        term = format_term(term)
        term_len = len(term)
        can_search_keys = term_len >= min(MIN_TERM_FOR_SEARCH_CONTAINS, MIN_TERM_FOR_SEARCH_CONTAINS)
        if not can_search_keys:
            return [term]
        keys = []
        search_start = term_len >= MIN_TERM_FOR_SEARCH_START
        search_contains = term_len >= MIN_TERM_FOR_SEARCH_CONTAINS
        for key in self.storage.keys():
            if len(key) < len(term):
                pass
            elif key == term:
                return [key]
            elif search_start and key[:term_len] == term:
                keys.append(key)
            elif search_contains and term in key:
                keys.append(key)
        return keys
