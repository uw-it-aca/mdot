from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import resolve


class MdotdevTest(TestCase):
    """
    Test for the functionality of the views and the urls.
    """

    def setUp(self):
        self.client = Client()
        pass

    def test_url_home(self):
        """
        Test that request to home url sends the user to home view.
        """
        resolver = resolve('/developers/')
        self.assertEqual('home', resolver.view_name)

    def test_url_guidelines(self):
        """
        Test that request to guidelines url sends the user to
        guidelines view.
        """
        resolver = resolve('/developers/guidelines/')
        self.assertEqual('guidelines', resolver.view_name)

    def test_url_process(self):
        """
        Test that request to process url sends the user to
        process view.
        """
        resolver = resolve('/developers/process/')
        self.assertEqual('process', resolver.view_name)

    def test_url_review(self):
        """
        Test that request to review url sends the user to
        guidelines view.
        """
        resolver = resolve('/developers/review/')
        self.assertEqual('review', resolver.view_name)

    def test_view_home(self):
        """
        Test that request to home url returns a status code
        of 200.
        """
        response = self.client.get('/developers/')
        self.assertEqual(response.status_code, 200)

    def test_view_guidelines(self):
        """
        Test that request to guidelines url returns a status code
        of 200.
        """
        response = self.client.get('/developers/guidelines/')
        self.assertEqual(response.status_code, 200)

    def test_view_process(self):
        """
        Test that request to process url returns a status code
        of 200.
        """
        response = self.client.get('/developers/process/')
        self.assertEqual(response.status_code, 200)

    def test_view_review(self):
        """
        Test that request to review url returns a status code
        of 200.
        """
        response = self.client.get('/developers/review/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
