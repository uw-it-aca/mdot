from datetime import datetime

import random
import time
from django.contrib.auth.models import User
from mdot.models import Sponsor, Manager, App, Platform, Agreement
from mdot.admin import AgreementFilter, AgreementAdmin


class MdotTimedAdminTest():
    """
    Timed tests that cover the efficiency of mdot's
    admin site.
    """

    def setUp(self):
        App.objects.all().delete()
        Agreement.objects.all().delete()
        Manager.objects.all().delete()
        Sponsor.objects.all().delete()
        Platform.objects.all().delete()
        User.objects.all().delete()

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
            netid='spontest',
            email='sponsor@uw.edu'
        )
        self.manager = Manager.objects.create(
            first_name='J',
            last_name='average',
            netid='mantest',
            email='manager@uw.edu'
        )
        self.app = App.objects.create(
            name='TestApp',
            primary_language='English',
            app_manager=self.manager,
            app_sponsor=self.sponsor,
            requestor=self.user,
        )

    def test_agreement_filter_timeliness(self):
        """
        Test that checks that the agreement filter filters in a reasonable
        time with a large amount of Apps
        """

        App.objects.all().delete()
        Agreement.objects.all().delete()
        apps, agreements = [], []
        statuses = ['agreed', 'denied', 'removed']
        for i in range(1000):
            apps.append(App.objects.create(
                name='TestApp' + str(i),
                primary_language='English',
                app_manager=self.manager,
                app_sponsor=self.sponsor,
                requestor=self.user,
            ))

            agreements.append(Agreement.objects.create(
                app=apps[i],
                status=statuses[random.randint(0, 2)]
            ))

        start = time.time()
        agreeds = AgreementFilter(
            None,
            {'status': 'agreed'},
            Agreement,
            AgreementAdmin
        )
        denieds = AgreementFilter(
            None,
            {'status': 'denied'},
            Agreement,
            AgreementAdmin
        )
        removeds = AgreementFilter(
            None,
            {'status': 'removed'},
            Agreement,
            AgreementAdmin
        )
        pendings = AgreementFilter(
            None,
            {'status': 'pending'},
            Agreement,
            AgreementAdmin
        )
        print(len(pendings.queryset(None, App.objects.all())))
        print(len(agreeds.queryset(None, App.objects.all())))
        print(len(denieds.queryset(None, App.objects.all())))
        print(len(removeds.queryset(None, App.objects.all())))
        end = time.time()
        print('\ntime taken: ' + str(end - start))
        self.assertTrue(end - start < 30)

    def tearDown(self):
        pass
                                                                                                                                                                           
