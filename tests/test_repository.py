import unittest

import address_book
from address_book import models


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.repository = address_book.create_book()

    def test_search_by_empty_email(self):
        person = models.Person('', '')
        self.repository.save(person)
        person.emails = ['', ]
        result = self.repository.find_persons_by_email('')
        self.assertEqual(len(list(result)), 0)

    def test_search_by_name(self):
        last = models.Person('first', 'last')
        second = models.Person('fi\'rst', 'second')
        one = models.Person('one', '  f irst')
        no_name = models.Person('first1', '2first')
        self.repository.save(last)
        self.repository.save(second)
        self.repository.save(one)
        self.repository.save(no_name)
        result = self.repository.find_persons_by_name('first')
        self.assertEqual(len(result), 3)
        self.assertIn(last, result)
        self.assertIn(second, result)
        self.assertIn(one, result)

    def test_find_by_full_email(self):
        first = models.Person('n1', 'n2', emails=['example@test.test', 'my@test.test'])
        second = models.Person('n2', 'n2', emails=['example@test.test2'])
        self.repository.save(first)
        self.repository.save(second)
        result = self.repository.find_persons_by_email('example@test.test')
        self.assertEqual(len(result), 1)
        self.assertIn(first, result)

    def test_find_by_part_of_email(self):
        first = models.Person('n1', 'n2', emails=['my-example@test.test', 'my@test.test'])
        second = models.Person('n2', 'n2', emails=['example@test.test2'])
        self.repository.save(first)
        self.repository.save(second)
        result = self.repository.find_persons_by_email('example@test.test')
        self.assertEqual(len(result), 2)
        self.assertIn(first, result)
        self.assertIn(second, result)

    def test_not_results_of_find_by_email(self):
        first = models.Person('n1', 'n2', emails=['example@test.test', 'my@test.com'])
        second = models.Person('n2', 'n2', emails=['example@test.test'])
        self.repository.save(first)
        self.repository.save(second)
        result = self.repository.find_persons_by_email('example@test.com')
        self.assertEqual(len(result), 0)
