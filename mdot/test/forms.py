# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import Client, TestCase
from django.contrib.auth.models import User
from mdot.models import SponsorForm, ManagerForm, \
    AppForm, Platform, App, Sponsor, Manager


class MdotFormTest(TestCase):
    """
    Tests that cover the functionality of the
    Request Form.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="javerage",
            email="javerage@uw.edu",
            password="p@ssTest1"
        )
        self.platform = Platform.objects.create(
            name='Android',
            app_store='Google Play Store'
        )

    def test_sponsor_form_input_consumption(self):
        """
        Test that the sponsor forms is valid when passed
        all required values.
        """

        sponsor_form_data = {
            'first_name': 'Sponsor',
            'last_name': 'lname',
            'netid': 'spontest',
            'email': 'spon@uw.edu',
            'title': 'Sponsor Test Case',
            'department': 'sponsor testcase',
            'unit': 'Sponsor Test Case'}
        sponsor_form = SponsorForm(data=sponsor_form_data)
        self.assertTrue(sponsor_form.is_valid())

    def test_sponsor_form_duplicate(self):
        """
        Test that the sponsor forms is valid when passed
        a form with the same netid twice.
        """

        sponsor_form_data = {
            'first_name': 'Sponsor',
            'last_name': 'lname',
            'netid': 'spontest',
            'email': 'spon@uw.edu',
            'title': 'Sponsor Test Case',
            'department': 'sponsor testcase',
            'unit': 'Sponsor Test Case'}
        sponsor_form_1 = SponsorForm(data=sponsor_form_data)
        sponsor_form_2 = SponsorForm(data=sponsor_form_data)
        self.assertTrue(sponsor_form_1.is_valid())
        self.assertTrue(sponsor_form_2.is_valid())

    def test_sponsor_form_invalid_netid(self):
        """
        Test that the sponsor form does not accept a
        UW NetID that contains any non-alphanumeric
        characters
        """

        sponsor_form_data = {
            'first_name': 'Sponsor',
            'last_name': 'lname',
            'netid': 'SponTest@uw.edu',
            'title': 'Sponsor Test Case',
            'email': 'spontestcase@uw.edu',
            'department': 'sponsor testcase',
            'unit': 'Sponsor Test Case'}
        sponsor_form = SponsorForm(data=sponsor_form_data)
        self.assertFalse(sponsor_form.is_valid())

    def test_manager_form_input_consumption(self):
        """
        Test that the manager form is valid when passed
        all required values.
        """
        manager_form_data = {
            'first_name': 'Manager',
            'last_name': 'lname',
            'netid': 'mantest',
            'email': 'manager@uw.edu'}
        manager_form = ManagerForm(data=manager_form_data)
        self.assertTrue(manager_form.is_valid())

    def test_manager_form_invalid_netid(self):
        """
        Test that the manager form does not accept a
        UW NetID that contains any non-alphanumeric
        characters
        """

        manager_form_data = {
            'first_name': 'Manager',
            'last_name': 'lname',
            'netid': 'ManTest@uw.edu',
            'email': 'manager@uw.edu'}
        manager_form = ManagerForm(data=manager_form_data)
        self.assertFalse(manager_form.is_valid())

    def test_app_form_input_consumption(self):
        """
        Test that the app form is valid when passed
        all required values.
        """
        app_form_data = {
            'name': 'App',
            'primary_language': 'Test Lang',
            'platform': [self.platform.pk]
        }
        app_form = AppForm(data=app_form_data)
        self.assertTrue(app_form.is_valid())

    def test_full_valid_form_post(self):
        """
        Test that when given a complete, valid form the view
        sends the user to the thank you page.
        """

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms = {
            '{}first_name'.format(sponsor_prefix): 'Sponsor',
            '{}last_name'.format(sponsor_prefix): 'lname',
            '{}netid'.format(sponsor_prefix): 'spontest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Manager',
            '{}last_name'.format(manager_prefix): 'lname',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        # login user
        self.client.force_login(self.user)
        response = self.client.post('/developers/request/', forms)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank You' in response.content)

    def test_full_invalid_netid_form_post(self):
        """
        Test that when given a complete form with an invalid
        NetID, the view sends the user back to the request page.
        """

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms = {
            '{}first_name'.format(sponsor_prefix): 'Sponsor',
            '{}last_name'.format(sponsor_prefix): 'lname',
            '{}netid'.format(sponsor_prefix): 'SponTest@uw.edu',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Manager',
            '{}last_name'.format(manager_prefix): 'lname',
            '{}netid'.format(manager_prefix): 'manager@uw.edu',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        # login user
        self.client.force_login(self.user)
        response = self.client.post('/developers/request/', forms)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is not sent to the thank you
        # page after submitting an invalid netid in form
        self.assertFalse(b'Thank You' in response.content)

    def test_full_valid_form_post_with_reused_sponsor(self):
        """
        Test that when given a complete, valid form the view
        sends the user to the thank you page and reuses an existing
        Sponsor if the netid is already used.
        """

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms_1 = {
            '{}first_name'.format(sponsor_prefix): 'Real',
            '{}last_name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'spontest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'First',
            '{}last_name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager1',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        forms_2 = {
            '{}first_name'.format(sponsor_prefix): 'Second',
            '{}last_name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'spontest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Second',
            '{}last_name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager2',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        # login user
        self.client.force_login(self.user)
        response_1 = self.client.post('/developers/request/', forms_1)
        response_2 = self.client.post('/developers/request/', forms_2)
        self.assertTrue(not Sponsor.objects.filter(first_name='Second'))
        self.assertTrue(Sponsor.objects.filter(first_name='Real'))
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank You' in response_1.content)
        self.assertTrue(b'Thank You' in response_2.content)

    def test_full_valid_form_post_with_reused_manager(self):
        """
        Test that when given a complete, valid form the view
        sends the user to the thank you page and reuses an existing
        Sponsor if the netid is already used.
        """

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms_1 = {
            '{}first_name'.format(sponsor_prefix): 'First',
            '{}last_name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'spontes1',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Real',
            '{}last_name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        forms_2 = {
            '{}first_name'.format(sponsor_prefix): 'Second',
            '{}last_name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'spontes2',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Second',
            '{}last_name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}platform'.format(app_prefix): [self.platform.pk],
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        # login user
        self.client.force_login(self.user)
        response_1 = self.client.post('/developers/request/', forms_1)
        response_2 = self.client.post('/developers/request/', forms_2)
        self.assertTrue(not Manager.objects.filter(first_name='Second'))
        self.assertTrue(Manager.objects.filter(first_name='Real'))
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank You' in response_1.content)
        self.assertTrue(b'Thank You' in response_2.content)

    def tearDown(self):
        pass
