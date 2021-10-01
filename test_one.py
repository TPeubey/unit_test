import unittest


def person_number(person_count: int) -> int:
    return person_count


def get_pizza_number() -> int:
    return 2


def get_number_slice_by_people(people: int, pizza: int) -> int:
    default_slice_by_pizza = 8
    return pizza * default_slice_by_pizza // people


class TestOne(unittest.TestCase):

    def test_get_person_return_input_people_given(self):
        self.assertEqual(8, person_number(8))

    def test_get_pizza_number(self):
        number_pizza = get_pizza_number()
        self.assertEqual(2, number_pizza)

    def test_number_slice_by_people_with_2_pizza_8_people(self):
        number_slice_by_people = get_number_slice_by_people(people=8, pizza=2)
        self.assertEqual(2, number_slice_by_people)

    def test_even(self):
        
