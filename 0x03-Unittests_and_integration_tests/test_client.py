#!/usr/bin/env python3
"""
Task 4: Parameterize and patch as decorators
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_request):
        """
        get_json is called once with the expected
        argument but make sure it is not executed
        """
        obj = GithubOrgClient(org_name)
        obj.org()
        mock_request.assert_called_once_with(obj.ORG_URL.format(org=org_name))
