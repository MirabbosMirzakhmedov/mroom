from django.core.management import base
from datetime import datetime
from django.utils import timezone



class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print('run playground')
