import unittest

def person_number(person_count):
    return person_count

class TestOne(unittest.TestCase):

    def test_first(self):

        self.assertEqual(8, person_number(8))

