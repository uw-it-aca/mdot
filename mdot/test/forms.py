from django.test import Client, TestCase
from django.contrib.auth.models import User
from mdot.models import SponsorForm, ManagerForm, AppForm, Platform, App


class MdotFormTest(TestCase):
    """
    Tests that cover the fuctionality of the
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

    def test_form_input_consumption(self):
        """
        Test that the forms are valid when passed
        all required values.
        """

        sponsor_form_data = {
            'first_name': 'Sponsor',
            'last_name': 'lname',
            'netid': 'SponTest',
            'email': 'spon@uw.edu',
            'title': 'Sponsor Test Case',
            'email': 'spontestcase@uw.edu',
            'department': 'sponsor testcase',
            'unit': 'Sponsor Test Case'}
        sponsor_form = SponsorForm(data=sponsor_form_data)
        self.assertTrue(sponsor_form.is_valid())

        manager_form_data = {
            'first_name': 'Manager',
            'last_name': 'lname',
            'netid': 'ManTest',
            'email': 'manager@uw.edu'}
        manager_form = ManagerForm(data=manager_form_data)
        self.assertTrue(manager_form.is_valid())

        app_form_data = {
            'name': 'App',
            'primary_language': 'Test Lang',
            'platform': [self.platform.pk]
        }
        app_form = AppForm(data=app_form_data)
        self.assertTrue(app_form.is_valid())

    def test_minimal_valid_form_post(self):
        """
        Test that when given a minimal but valid form the view
        sends the user to the thank you page.
        """

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms = {
            '{}first_name'.format(sponsor_prefix): 'Sponsor',
            '{}last_name'.format(sponsor_prefix): 'lname',
            '{}netid'.format(sponsor_prefix): 'SponTest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}first_name'.format(manager_prefix): 'Manager',
            '{}last_name'.format(manager_prefix): 'lname',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'man@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}primary_language'.format(app_prefix): 'Test Lang',
            '{}platform'.format(app_prefix): [self.platform.pk]
        }

        # login user
        self.client.force_login(self.user)
        response = self.client.post('/developers/request/', forms)
        self.assertEqual(response.status_code, 200)

        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank You' in response.content)

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
            '{}netid'.format(sponsor_prefix): 'SponTest',
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

    def tearDown(self):
        pass
