"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mdot.mdot_rest_client.client import MDOT


class MdotClientTest(TestCase):
    def setUp(self):
        pass

    def test_get_resources(self):
        """
        Tests the client that retrieves data from the mdot API.
        """
        #TODO: make sure to patch settings to always use file based for unit tests
        resources = MDOT().get_resources()
        # Make sure what we get back is a list
        self.assertEqual(type(resources), type([]))
        # Make sure that the list items are dicts
        self.assertEqual(type(resources[0]), type({}))
        # Make sure the resource title is unicode
        self.assertEqual(type(resources[0]['title']), type(u'string'))

    def tearDown(self):
        pass
