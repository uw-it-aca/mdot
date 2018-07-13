from django.test import Client, TestCase
from mdot.forms import ReviewForm


class MdotFormTest(TestCase):
    """
    Tests that cover the fuctionality of the
    Review Form.
    """

    def setUp(self):
        self.client = Client()

    def test_form_input_consumption(self):
        """
        Test that the form is valid when passed
        all required values.
        """
        form_data = {
            'campus_audience': 'Student',
            'campus_need': 'Test',
            'sponsor_name': 'Test Case',
            'sponsor_netid': 'testcase',
            'sponsor_email': 'testcase@uw.edu',
            'dev_name': 'Test Case',
            'dev_email': 'testcase@uw.edu',
            'support_name': 'Test Case',
            'support_email': 'testcase@uw.edu',
            'app_code': '<?php ?>'}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_minimal_valid_form_post(self):
        """
        Test that when given a minimal but valid form the view
        sends the user to the thank you page.
        """
        form_data = {
            'campus_audience': 'Student',
            'campus_need': 'Test',
            'sponsor_name': 'Test Case',
            'sponsor_netid': 'testcase',
            'sponsor_email': 'testcase@uw.edu',
            'dev_name': 'Test Case',
            'dev_email': 'testcase@uw.edu',
            'support_name': 'Test Case',
            'support_email': 'testcase@uw.edu',
            'app_code': '<?php ?>'}
        form = ReviewForm(data=form_data)
        response = self.client.post('/developers/review/', form_data)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue('Thank you' in response.content)

    def test_full_valid_form_post(self):
        """
        Test that when given a complete, valid form the view
        sends the user to the thank you page.
        """

        form_data = {
            'campus_audience': 'Student',
            'campus_need': 'Test',
            'sponsor_name': 'Test Case',
            'sponsor_netid': 'testcase',
            'sponsor_email': 'testcase@uw.edu',
            'dev_name': 'Test Case',
            'dev_email': 'testcase@uw.edu',
            'support_name': 'Test Case',
            'support_email': 'testcase@uw.edu',
            'support_contact': 'test',
            'ats_review': True,
            'ux_review': True,
            'brand_review': True,
            'app_documentation': 'http://spacescout.uw.edu',
            'app_code': '<?php ?>',
            'anything_else': 'This is a test.'}
        form = ReviewForm(data=form_data)
        response = self.client.post('/developers/review/', form_data)
        self.assertEqual(response.status_code, 200)
        # Make sure the user is sent to the thank you
        # page after submitting valid form
        self.assertTrue('Thank you' in response.content)

    def test_bad_header(self):
        """
        Test that when given incorrect data the request contains
        'Invalid header found.'.

        The new line character in the sponsor_name is
        what causes the error.
        """

        form_data = {
            'campus_audience': 'Student',
            'campus_need': 'Test',
            'sponsor_name': 'Test\n Case',
            'sponsor_netid': 'testcase',
            'sponsor_email': 'testcase@uw.edu',
            'dev_name': 'Test Case',
            'dev_email': 'testcase@uw.edu',
            'support_name': 'Test Case',
            'support_email': 'testcase@uw.edu',
            'support_contact': 'test',
            'ats_review': True,
            'ux_review': True,
            'brand_review': True,
            'app_documentation': 'http://spacescout.uw.edu',
            'app_code': '<?php ?>',
            'anything_else': 'This is a test.'}
        response = self.client.post('/developers/review/', form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid header found.')

    def test_review_get(self):
        """
        Test that a get request to the url will send the user
        to the form.
        """
        response = self.client.get('/developers/review/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Submit your App for Review' in response.content)

    def tearDown(self):
        pass
