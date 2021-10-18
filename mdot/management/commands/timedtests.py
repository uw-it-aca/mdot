from datetime import datetime
import random
import time

from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.contrib.auth.models import User
from mdot.models import Sponsor, Manager, App, Platform, Agreement
from mdot.admin import AgreementFilter, AgreementAdmin


def _test_agreement_filter_timeliness():
    """
    Test that checks that the agreement filter filters in a reasonable
    time with a large amount of Apps
    """

    App.objects.all().delete()
    Agreement.objects.all().delete()
    Manager.objects.all().delete()
    Sponsor.objects.all().delete()
    Platform.objects.all().delete()
    User.objects.all().delete()

    requestor=User.objects.create_user(
        username="javerage",
        email="javerage@uw.edu",
        password="p@assTest1",
    )

    apps, agreements = [], []
    statuses = ['agreed', 'denied', 'removed']
    for i in range(1000):
        apps.append(App.objects.create(
            name='TestApp' + str(i),
            primary_language='English',
            app_manager=Manager.objects.create(
                first_name='J',
                last_name='average',
                netid='mantest',
                email='manager@uw.edu'
            ),
            app_sponsor=Sponsor.objects.create(
                first_name='Sponsor',
                last_name='lname',
                netid='spontest',
                email='sponsor@uw.edu'
            ),
            requestor=requestor
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
    print('\nQueryset lengths (out of 1000):')
    print(len(pendings.queryset(None, App.objects.all())))
    print(len(agreeds.queryset(None, App.objects.all())))
    print(len(denieds.queryset(None, App.objects.all())))
    print(len(removeds.queryset(None, App.objects.all())))
    end = time.time()
    print('\ntime taken: ' + str(end - start) + ' seconds')


class Command(BaseCommand):
    help = 'Runs tests to check the timeliness of MDOT'
    
    def handle(self, *args, **options):
        _test_agreement_filter_timeliness()
        self.stdout.write(self.style.SUCCESS('Completed'))

