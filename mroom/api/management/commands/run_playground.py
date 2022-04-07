from django.core.management import base


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print('This is a run_playground')
