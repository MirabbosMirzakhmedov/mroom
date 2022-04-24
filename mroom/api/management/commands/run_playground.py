from django.core.management import base

from mroom.report.models import Question, Answer, Survey


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print('This is a playground')
