from django.core.management import base
import os
import base64


class Command(base.BaseCommand):

    def handle(self, *args, **options):
        print(base64.urlsafe_b64encode(s=os.urandom(64)))



def gen_token(byte_length: int) -> str:
    token = base64.urlsafe_b64encode(s=os.urandom(byte_length))

    return token.decode()

