from django.test import Client, TestCase, override_settings
from django.core.urlresolvers import resolve

DAO = 'Mock'


@override_settings(RESTCLIENTS_MDOT_DAO_CLASS=DAO)
class MdotTest(TestCase):
    """
    Test for the functionality of the views and the urls.
    """

    def setUp(self):
        self.client = Client()
        pass

    # test "/" url and view
    def test_home_url(self):
        resolver = resolve('/')
        self.assertEqual('home', resolver.view_name)

    def test_home_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    # test "/developers" url and view
    def test_dev_home_url(self):
        """
        Test that request to home url sends the user to home view.
        """
        resolver = resolve('/developers/')
        self.assertEqual('developers', resolver.view_name)

    def test_dev_home_view(self):
        """
        Test that request to home url returns a status code
        of 200.
        """
        response = self.client.get('/developers/')
        self.assertEqual(response.status_code, 200)

    # test "/developers/guidelines" url and view
    def test_dev_guidelines_url(self):
        """
        Test that request to guidelines url sends the user to
        guidelines view.
        """
        resolver = resolve('/developers/guidelines/')
        self.assertEqual('guidelines', resolver.view_name)

    def test_dev_guidelines_view(self):
        """
        Test that request to guidelines url returns a status code
        of 200.
        """
        response = self.client.get('/developers/guidelines/')
        self.assertEqual(response.status_code, 200)

    def test_dev_process_url(self):
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
