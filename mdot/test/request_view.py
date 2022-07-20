# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import Client, TestCase
from django.contrib.auth.models import User
from mdot.models import SponsorForm, ManagerForm, AppForm,\
    Platform, App, Sponsor, Manager, Agreement


class MdotRequestTest(TestCase):
    """
    Tests that cover the functionality of the
    Request Form.
    """

    def setUp(self):
        self.client = Client()
        self.app_sponsor = User.objects.create_user(
            username="javerage",
            email="javerage@uw.edu",
            password="p@ssTest1"
        )
        self.requestor = User.objects.create_user(
            username="testuser",
            email="testuser@uw.edu",
            password="p@ssTest2"
        )

        self.platform = Platform.objects.create(
            name='Android',
            app_store='Google Play Store'
        )
        self.sponsor = Sponsor.objects.create(
            first_name="sponsor",
            last_name="last name",
            netid="javerage",
            email="javerage@uw.edu",
            title="title",
            department="department",
            unit="unit"
        )
        self.manager = Manager.objects.create(
            first_name="manager",
            last_name="last name",
            netid="man",
            email="man@uw.edu"
        )
        self.app = App.objects.create(
            name="app name",
            primary_language="English",
            app_manager=self.manager,
            app_sponsor=self.sponsor,
            requestor=self.requestor,
        )
        self.app.platform.add(self.platform)

    def test_view_correct_sponsor(self):
        """
        Test checks that the sponsor can access the sponsor
        agreement form page
        """
        pk = self.app.pk

        # login javerage and try to navigate to correct url
        self.client.force_login(self.app_sponsor)
        response = self.client.get("/developers/request/{}/".format(pk))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_view_incorrect_sponsor(self):
        """
        Test checks that user who is not the sponsor cannot access
        the sponsor agreement form page
        """
        pk = self.app.pk

        # login javerage and try to navigate to correct url
        self.client.force_login(self.requestor)
        response = self.client.get("/developers/request/{}/".format(pk))
        self.assertEqual(response.status_code, 403)
        self.client.logout()

    def test_view_accept_sponsorship(self):
        """
        Tests that the sponsor agreement page successfully submits
        when all checkboxes are selected. Page should redirect to
        a Thank You page
        """
        pk = self.app.pk

        self.client.force_login(self.app_sponsor)

        # checkbox values
        params = {
            "sponsor-requirements": "on",
            "understand-agreements": "on",
            "understand-manager": "on",
            "agree": "on"
        }
        response = self.client.post("/developers/request/{}/".format(pk),
                                    params)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Thank You" in response.content)
        # check that agreement object was created
        self.assertTrue(Agreement.objects.filter(app__pk=pk).exists())

        # accessing the original request page should redirect to Thank you page
        response = self.client.get("/developers/request/{}/".format(pk))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Thank You" in response.content)

    def test_view_unchecked_accept_sponsorship(self):
        """
        Tests that the sponsor agreement object is not created if post request
        is not submitted with all checkboxes.
        """
        pk = self.app.pk

        self.client.force_login(self.app_sponsor)

        # checkbox values
        params = {
            "sponsor-requirements": "on"
        }
        response = self.client.post("/developers/request/{}/".format(pk),
                                    params)
        # make sure agreement is not made for app
        self.assertFalse(Agreement.objects.filter(app__pk=pk).exists())

    def test_decline_sponsorship(self):
        """
        Tests that the decline page creates an agreement object
        with 'denied' as the agree value
        """
        pk = self.app.pk

        self.client.force_login(self.app_sponsor)

        response = self.client.get("/developers/decline/{}/".format(pk))
        self.assertEqual(response.status_code, 200)
        # make sure agreement object is created with 'false' for agree value
        self.assertTrue(Agreement.objects.filter(app__pk=pk).exists())
        self.assertEquals(Agreement.objects.get(app__pk=pk).status, 'denied')

        # accessing the original request page should redirect to Thank you page
        response = self.client.get("/developers/request/{}/".format(pk))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Thank You" in response.content)

    def test_incorrect_sponsor_decline(self):
        """
        Test checks that user who is not the sponsor cannot access
        the decline page
        """
        pk = self.app.pk

        # login javerage and try to navigate to correct url
        self.client.force_login(self.requestor)
        response = self.client.get("/developers/decline/{}/".format(pk))
        self.assertEqual(response.status_code, 403)
        self.client.logout()

    def test_app_does_not_exist(self):
        """
        Test check that 404 status code is returned when trying to access
        a view for an app that does not exist
        """
        pk = self.app.pk
        nonexistant_pk = pk + 1

        self.client.force_login(self.app_sponsor)
        response = self.client.get(
            "/developers/request/{}/".format(nonexistant_pk))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(
            "/developers/decline/{}/".format(nonexistant_pk))
        self.assertEqual(response.status_code, 404)

    def test_submitting_removes_duplicate_sponsor(self):
        """
        Test to check that submitting a request form with an existing
        Sponsor doesn't create a duplicate Sponsor.
        """

        self.client.request(app=self.app,
                            sponsor=self.sponsor,
                            manager=self.manager)
        self.client.request(app=self.app,
                            sponsor=self.sponsor,
                            manager=self.manager)
        self.assertEqual(
            len(Sponsor.objects.filter(netid=self.sponsor.netid)),
            1
        )

    def test_submitting_removes_duplicate_manager(self):
        """
        Test to check that submitting a request form with an existing
        Manager doesn't create a duplicate Sponsor.
        """

        self.client.request(app=self.app,
                            sponsor=self.sponsor,
                            manager=self.manager)
        self.client.request(app=self.app,
                            sponsor=self.sponsor,
                            manager=self.manager)
        self.assertEqual(
            len(Manager.objects.filter(netid=self.manager.netid)),
            1
        )

    def tearDown(self):
        pass
