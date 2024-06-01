#!/usr/bin/env python3
"""
Task 0: Parameterize a unit test
"""
import unittest
from unittest.mock import patch, Mock
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """
        test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Mock HTTP calls
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, make_request):
        """
        test that utils.get_json returns the expected result
        """
        mock_response = make_request.get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test memoize
    """
    def test_memoize(self):
        """
        a_method is only called once
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_method:
            obj = TestClass()
            obj.a_property()
            obj.a_property()
            mock_method.assert_called_once()
