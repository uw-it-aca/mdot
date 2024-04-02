# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import Client, TestCase, override_settings
from django.urls import resolve
from django.contrib.auth.models import User

DAO = 'Mock'


@override_settings(RESTCLIENTS_MDOT_DAO_CLASS=DAO)
class MdotTest(TestCase):
    """
    Test for the functionality of the views and the urls.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="javerage",
            email="javerage@uw.edu",
            password="p@ssTest1"
        )
        pass

    # test "/" url and view
    def test_home_url(self):
        resolver = resolve('/')
        self.assertEqual('home', resolver.view_name)

    def test_home_view(self):
        response = self.client.get('/')
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

    def test_url_request(self):
        """
        Test that request to request url sends the user to
        guidelines view.
        """
        resolver = resolve('/developers/request/')
        self.assertEqual('request', resolver.view_name)

    def test_view_process(self):
        """
        Test that request to process url returns a status code
        of 200.
        """
        response = self.client.get('/developers/process/')
        self.assertEqual(response.status_code, 200)

    def test_view_request_not_logged_in(self):
        """
        Test that request to request url returns a status code
        of 302 when user is not logged in.
        """
        response = self.client.get('/developers/request/')
        self.assertEqual(response.status_code, 302)

    def test_view_request_logged_in(self):
        """
        Test that request to request url returns a status code
        of 200 when user is logged in.
        """
        self.client.force_login(self.user)
        response = self.client.get('/developers/request/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def tearDown(self):
        pass
