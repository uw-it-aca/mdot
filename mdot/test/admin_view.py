from datetime import datetime

from django.test import Client, TestCase
from django.contrib.auth.models import User
from mdot.models import Sponsor, Manager, App, Platform, Agreement


class MdotAdminTest(TestCase):
    """
    Tests that cover the functionality of mdot's
    admin site.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="javerage",
            email="javerage@uw.edu",
            password="p@ssTest1"
        )
        self.platform_android = Platform.objects.create(
            name='Android',
            app_store='Google Play Store'
        )
        self.platform_ios = Platform.objects.create(
            name='IOS',
            app_store='Apple Store'
        )
        self.sponsor = Sponsor.objects.create(
            first_name='Sponsor',
            last_name='lname',
            email='sponsor@uw.edu'
        )
        self.manager = Manager.objects.create(
            first_name='J',
            last_name='average',
            email='manager@uw.edu'
        )
        self.app = App.objects.create(
            name='TestApp',
            primary_language='English',
            app_manager=self.manager,
            app_sponsor=self.sponsor,
            requestor=self.user,
        )

    def test_platform_name_displays_properly(self):
        """
        Test that the platform's name in the Platform admin link
        displays the app store name correctly.
        """

        platform = Platform(name='Incorrect', app_store='Android')
        self.assertEqual('Android', str(platform))

    def test_sponsor_name_displays_properly(self):
        """
        Test that the sponsor's name in the Sponsor admin link
        displays the full name correctly.
        """

        self.assertEqual('Sponsor lname', str(self.sponsor))

    def test_manager_name_displays_properly(self):
        """
        Test that the manager's name in the Manager admin link
        displays the full name correctly.
        """

        self.assertEqual('J average', str(self.manager))

    def test_app_name_displays_properly(self):
        """
        Test that the app's name in the App admin link
        displays the app's name correctly.
        """

        self.assertEqual('TestApp', str(self.app))

    def test_manager_contact_displays_properly(self):
        """
        Test that app manager's email in detail view displays
        properly.
        """

        display = self.app.manager_contact
        self.assertEqual('manager@uw.edu', display)

    def test_sponsor_contact_displays_properly(self):
        """
        Test that app sponsor's email in detail view displays
        properly.
        """

        display = self.app.sponsor_contact
        self.assertEqual('sponsor@uw.edu', display)

    def test_agreement_name_displays_properly(self):
        """
        Test that the agreement's app name in the Agreements admin link
        displays correctly.
        """

        agreement = Agreement(app=self.app, agree=True)
        self.assertEqual('TestApp', str(agreement))

    def test_agreed_status_displays_properly(self):
        """
        Test that an approved app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement.objects.create(
            app=self.app,
            agree=True,
            agree_time=time
        )
        display = self.app.status()
        self.assertEqual(
            'Agreed on ' + time.strftime('%b %d, %Y, %I:%M %p'),
            str(display)
        )

    def test_denied_status_displays_properly(self):
        """
        Test that a denied app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement.objects.create(
            app=self.app,
            agree=False,
            agree_time=time
        )
        display = self.app.status()
        self.assertEqual(
            'Denied on ' + time.strftime('%b %d, %Y, %I:%M %p'),
            str(display)
        )

    def test_pending_status_displays_properly(self):
        """
        Test that a pending app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement(
            app=self.app,
            agree=False,
            agree_time=time
        )
        display = self.app.status()
        self.assertEqual('Pending', str(display))

    def test_app_platform_displays_properly(self):
        """
        Test that app platforms display properly on the admin dashboard.
        """

        self.app.platform.add(self.platform_ios, self.platform_android)
        display = self.app.app_platform()
        self.assertEqual('Google Play Store, Apple Store', str(display))

    def tearDown(self):
        pass
