"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mdot.mdot_rest_client.client import MDOT


class MdotClientTest(TestCase):
    def test_mdot_client(self):
        """
        Tests the client that retrieves data from the mdot API.
        """
        resources = MDOT().get_resources()
        self.assertEqual(resources.status, 200)
