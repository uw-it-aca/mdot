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
        self.platform = Platform.objects.create(
            name='Android',
            app_store='Google Play Store'
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

        sponsor = Sponsor(first_name='Sponsor', last_name='lname')
        self.assertEqual('Sponsor lname', str(sponsor))

    def test_manager_name_displays_properly(self):
        """
        Test that the manager's name in the Manager admin link
        displays the full name correctly.
        """

        manager = Manager(first_name='J', last_name='average')
        self.assertEqual('J average', str(manager))

    def test_app_name_displays_properly(self):
        """
        Test that the app's name in the App admin link
        displays the app's name correctly.
        """

        app = App(name='TestApp', primary_language='English')
        self.assertEqual('TestApp', str(app))

    def test_agreement_name_displays_properly(self):
        """
        Test that the agreement's app name in the Agreements admin link
        displays correctly.
        """

        app = App(name='TestApp', primary_language='English')

        agreement = Agreement(app=app, agree=True)
        self.assertEqual('TestApp', str(agreement))

    def tearDown(self):
        pass
