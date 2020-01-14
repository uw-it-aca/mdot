from django.test import Client, TestCase
from mdot.models import SponsorForm, ManagerForm, AppForm


class MdotFormTest(TestCase):
    """
    Tests that cover the fuctionality of the
    Request Form.
    """

    def setUp(self):
        self.client = Client()

    def test_form_input_consumption(self):
        """
        Test that the forms are valid when passed
        all required values.
        """
        sponsor_form_data = {
            'name': 'Sponsor',
            'netid': 'SponTest',
            'title': 'Sponsor Test Case',
            'email': 'spontestcase@uw.edu',
            'department': 'sponsor testcase',
            'unit': 'Sponsor Test Case'}
        sponsor_form = SponsorForm(data=sponsor_form_data)
        self.assertTrue(sponsor_form.is_valid())

        manager_form_data = {
            'name': 'Sponsor',
            'netid': 'SponTest',
            'email': 'spontestcase@uw.edu'}
        manager_form = ManagerForm(data=manager_form_data)
        self.assertTrue(manager_form.is_valid())

        app_form_data = {
            'name': 'Sponsor',
            'primary_language': 'Test Lang',
            'app_manager': manager_form,
            'app_sponsor': sponsor_form}
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
            '{}name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'SponTest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'managertestcase@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        response = self.client.post('/developers/request/', forms)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank you' in response.content)

    def test_full_valid_form_post(self):
        """
        Test that when given a complete, valid form the view
        sends the user to the thank you page.
        """
        
        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms = {
            '{}name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'SponTest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'managertestcase@uw.edu',

        sponsor_prefix = 'sponsor-'
        manager_prefix = 'manager-'
        app_prefix = 'app-'
        forms = {
            '{}name'.format(sponsor_prefix): 'Sponsor',
            '{}netid'.format(sponsor_prefix): 'SponTest',
            '{}title'.format(sponsor_prefix): 'Sponsor Test Case',
            '{}email'.format(sponsor_prefix): 'spontestcase@uw.edu',
            '{}department'.format(sponsor_prefix): 'sponsor testcase',
            '{}unit'.format(sponsor_prefix): 'Sponsor Test Case',

            '{}name'.format(manager_prefix): 'Manager',
            '{}netid'.format(manager_prefix): 'manager',
            '{}email'.format(manager_prefix): 'managertestcase@uw.edu',

            '{}name'.format(app_prefix): 'app',
            '{}primary_language'.format(app_prefix): 'Test Lang'
        }
        response = self.client.post('/developers/request/', forms)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue(b'Thank you' in response.content)

    def test_request_get(self):
        """
        Test that a get request to the url will send the user
        to the form.
        """
        response = self.client.get('/developers/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Request Review' in response.content)

    def tearDown(self):
        pass
