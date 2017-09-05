import unittest

from address_book import book
from address_book import models


class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.book = book.Book()

    def test_add_data(self):
        obj = models.Person('', '')
        self.book.add(obj)
        self.assertTrue(obj in self.book)

    def test_add_wrong_value(self):
        obj = dict()
        with self.assertRaises(TypeError):
            self.book.add(obj)

    def test_not_add_copies(self):
        obj = models.Person("first", "last")
        self.book.add(obj)
        self.book.add(obj)
        self.book.add(obj)
        self.assertEqual(len(self.book), 1)

    def test_contains(self):
        self.book.add(models.Person("name1", "name1"))
        self.book.add(models.Person("name2", "name2"))
        self.book.add(models.Group("name1"))
        self.book.add(models.Group("name2"))
        obj = models.Person("first", "last")
        self.book.add(obj)
        self.assertTrue(obj in self.book)

    def test_len_without_elements(self):
        self.assertEqual(len(self.book), 0)

    def test_len_with_elements(self):
        self.book.add(models.Person("name1", "name1"))
        self.book.add(models.Person("name2", "name2"))
        self.book.add(models.Group("name1"))
        self.book.add(models.Group("name2"))
        self.assertEqual(len(self.book), 4)

    def test_discard(self):
        self.book.add(models.Person("name1", "name1"))
        self.book.add(models.Person("name2", "name2"))
        self.book.add(models.Group("name1"))
        self.book.add(models.Group("name2"))
        obj = models.Person("first", "last")
        self.book.add(obj)
        self.assertTrue(obj in self.book)
        self.book.discard(obj)
        self.assertFalse(obj in self.book)

    def test_iter(self):
        values = [
            models.Person("name1", "name1"),
            models.Person("name2", "name2"),
            models.Group("name1"),
            models.Group("name2")
        ]
        list(map(self.book.add, values))
        count = 0
        for obj in self.book:
            count += 1
            self.assertTrue(obj in values)
            values.remove(obj)
        self.assertEqual(count, 4)

    def test_add_and_delete_person_with_groups(self):
        person = models.Person("first", "last")
        groups = [
            models.Group("group1"),
            models.Group("group2"),
            models.Group("group3"),
        ]
        list(map(person.groups.add, groups))
        self.book.add(person)
        self.assertEqual(len(self.book), 4)
        for group in groups:
            self.assertTrue(group in self.book)
            self.assertTrue(person in group.persons)
        self.book.discard(person)
        self.assertEqual(len(self.book), 0)
        self.assertFalse(person in self.book)
        for group in groups:
            self.assertFalse(group in self.book)
            self.assertFalse(person in group.persons)

    def test_add_and_delete_group_with_persons(self):
        group = models.Group('group')
        persons = [
            models.Person("name1", "name1"),
            models.Person("name2", "name2"),
            models.Person("name3", "name3"),
        ]
        list(map(group.persons.add, persons))
        self.book.add(group)
        self.assertEqual(len(self.book), 4)
        for person in persons:
            self.assertTrue(person in self.book)
            self.assertTrue(group in person.groups)
        self.book.discard(group)
        self.assertEqual(len(self.book), 3)
        self.assertFalse(group in self.book)
        for person in persons:
            self.assertTrue(person in self.book)
            self.assertFalse(group in person.groups)
