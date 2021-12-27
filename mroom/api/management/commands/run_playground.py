from django.core.management import base
from datetime import datetime
from django.utils import timezone



class Command(base.BaseCommand):

    def handle(self, *args, **options):
        time_now = datetime.now()
        date = '2021-12-27T22:17'

        # GOOGLE -> Turn string date time into python object
        # date_format = '2021-12-24T03:45'

        datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M")

        if time_now > datetime_object:
            print('Cannot insert old date')
