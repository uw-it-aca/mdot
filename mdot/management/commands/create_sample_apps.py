from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads sample app data to admin'

    def handle(self, *args, **options):
        call_command('loaddata', 'sample_apps.json')
        self.stdout.write(self.style.SUCCESS('Completed'))
