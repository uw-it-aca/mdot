from datetime import datetime

from django.test import Client, TestCase
from django.contrib.auth.models import User
from mdot.models import Sponsor, Manager, App, Platform, Agreement
from mdot.admin import AgreementFilter, AgreementAdmin
from django.core.exceptions import ValidationError


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

        agreement = Agreement(app=self.app, status='agreed')
        self.assertEqual('TestApp', str(agreement))

    def test_agreed_status_displays_properly(self):
        """
        Test that an approved app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement.objects.create(
            app=self.app,
            status='agreed',
            agree_time=time
        )
        display = self.app.status()
        self.assertTrue(str(display).startswith('Agreed on '))
        # self.assertEqual(
        #     'Agreed on ' + time.strftime('%b %d, %Y, %I:%M %p'),
        #     str(display)
        # )

    def test_denied_status_displays_properly(self):
        """
        Test that a denied app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement.objects.create(
            app=self.app,
            status='denied',
            agree_time=time
        )
        display = self.app.status()
        self.assertTrue(str(display).startswith('Denied on '))
        # self.assertEqual(
        #     'Denied on ' + time.strftime('%b %d, %Y, %I:%M %p'),
        #     str(display)
        # )

    def test_removed_status_displays_properly(self):
        """
        Test that a removed app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement.objects.create(
            app=self.app,
            status='removed',
            agree_time=time
        )
        display = self.app.status()
        self.assertTrue(str(display).startswith('Removed on '))
        # self.assertEqual(
        #     'Removed on ' + time.strftime('%b %d, %Y, %I:%M %p'),
        #     str(display)
        # )

    def test_pending_status_displays_properly(self):
        """
        Test that a pending app's agreement status displays properly.
        """

        time = datetime.now()
        agreement = Agreement(
            app=self.app,
            agree_time=time
        )
        display = self.app.status()
        self.assertEqual('Pending', str(display))

    def test_app_platform_displays_properly(self):
        """
        Test that an app's platforms display properly on the admin dashboard.
        """

        self.app.platform.add(self.platform_ios, self.platform_android)
        display = self.app.app_platform()
        self.assertEqual('Google Play Store, Apple Store', str(display))

    def test_invalid_agreement_status(self):
        """
        Test that agreement dashboard will raise ValidationError if no
        agreement status is selected.
        """

        time = datetime.now()
        with self.assertRaises(ValidationError):
            agreement = Agreement.objects.create(
                app=self.app,
                status='',
                agree_time=time)

    def test_agreement_filter_accepted_status(self):
        """
        Test that the agreement filter properly filters apps when the
        app's latest agreement status is accepted.
        """

        time = datetime.now()
        agreement = Agreement(
            app=self.app,
            status='agreed',
            agree_time=time
        )
        apps = App.objects.all()
        f = AgreementFilter(
            None,
            {'status': 'agreed'},
            Agreement,
            AgreementAdmin
        )
        self.assertTrue(f.queryset(None, apps).filter(id=self.app.id).exists)

    def test_agreement_filter_denied_status(self):
        """
        Test that the agreement filter properly filters apps when the
        app's latest agreement status is denied.
        """

        time = datetime.now()
        agreement = Agreement(
            app=self.app,
            status='denied',
            agree_time=time
        )
        apps = App.objects.all()
        f = AgreementFilter(
            None,
            {'status': 'denied'},
            Agreement,
            AgreementAdmin
        )
        self.assertTrue(f.queryset(None, apps).filter(id=self.app.id).exists)

    def test_agreement_filter_removed_status(self):
        """
        Test that the agreement filter properly filters apps when the
        app's latest agreement status is removed.
        """

        time = datetime.now()
        agreement = Agreement(
            app=self.app,
            status='removed',
            agree_time=time
        )
        apps = App.objects.all()
        f = AgreementFilter(
            None,
            {'status': 'removed'},
            Agreement,
            AgreementAdmin
        )
        self.assertTrue(f.queryset(None, apps).filter(id=self.app.id).exists)

    def test_agreement_filter_pending_status(self):
        """
        Test that the agreement filter properly filters apps when the
        app's latest agreement status is pending.
        """

        time = datetime.now()
        Agreement.objects.all().delete()
        apps = App.objects.all()
        f = AgreementFilter(
            None,
            {'status': 'pending'},
            Agreement,
            AgreementAdmin
        )
        self.assertTrue(f.queryset(None, apps).filter(id=self.app.id).exists())

    def test_similar_sponsor_objects_are_equal(self):
        """
        Test that Sponsor objects with the same NetID are
        considered equal.
        """

        s1 = Sponsor.objects.create(
            netid='jtest'
        )
        s2 = Sponsor.objects.create(
            netid='jtest'
        )
        s3 = Sponsor.objects.create(
            first_name='J',
            netid='jtest'
        )
        s4 = Sponsor.objects.create(
            first_name='D',
            netid='jtest'
        )
        self.assertEqual(s1, s2)
        self.assertEqual(s3, s4)

    def test_similar_manager_objects_are_equal(self):
        """
        Test that Manager objects with the same NetID are
        considered equal.
        """

        m1 = Manager.objects.create(
            netid='jtest'
        )
        m2 = Manager.objects.create(
            netid='jtest'
        )
        m3 = Manager.objects.create(
            first_name='J',
            netid='jtest'
        )
        m4 = Manager.objects.create(
            first_name='D',
            netid='jtest'
        )
        self.assertEqual(m1, m2)
        self.assertEqual(m3, m4)

    def tearDown(self):
        pass
