from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve


class MdotTest(TestCase):

    # Test that given url calls correct view
    def test_home_url(self):
        resolver = resolve('/')
        self.assertEqual('home', resolver.view_name)

    # Test that given url returns a 200 status code
    def test_home_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
