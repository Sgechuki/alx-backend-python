#!/usr/bin/env python3
"""
Task 0: Parameterize a unit test
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
     unit test for utils.access_nested_map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               output: Union[Dict, int]) -> None:
        """
        test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        """
        test that a KeyError is raised
        """
        self.assertRaises(exception, access_nested_map(nested_map, path))
