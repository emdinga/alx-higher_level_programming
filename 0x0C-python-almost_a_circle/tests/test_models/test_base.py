#!/usr/bin/python3
"""
Unit test for base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_incrementation(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_id_assignment(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_id_assignment_negative(self):
        base = Base(-5)
        self.assertEqual(base.id, -5)

    def test_id_assignment_float(self):
        base = Base(3.5)
        self.assertEqual(base.id, 3.5)

    def test_id_assignment_string(self):
        base = Base("abc")
        self.assertEqual(base.id, "abc")

    def test_to_json_string(self):
        base = Base(1)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]), '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'), [{"id": 1}, {"id": 2}])


if __name__ == '__main__':
    unittest.main()
