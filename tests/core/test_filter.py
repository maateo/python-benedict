# -*- coding: utf-8 -*-

from benedict.core import filter as _filter

import unittest


class filter_test_case(unittest.TestCase):

    def test_filter(self):
        i = {
            'a': 1,
            'b': 2,
            'c': '4',
            'e': '5',
            'f': 6,
            'g': 7,
        }
        with self.assertRaises(ValueError):
            f = _filter(i, True)
        o = _filter(i, lambda key, val: isinstance(val, int))
        r = {
            'a': 1,
            'b': 2,
            'f': 6,
            'g': 7,
        }
        self.assertFalse(i is o)
        self.assertEqual(o, r)
