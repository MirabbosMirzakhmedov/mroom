from django.test import TestCase
from rest_framework.test import APIClient
from typing import Dict
import json
from requests.exceptions import HTTPError
from mroom.api.models import User
import requests
from unittest.mock import patch


class TestSignup(TestCase):
    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'invalid_email',
            'password': '12345678',
            'name': 'Mirabbos',
            'terms': True
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'email': [
                    'Enter a valid email address.'
                ]
            }
        )

    def test_password_less_than_min_length(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '123',
            'name': 'Mirabbos',
            'terms': True
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has at least 8 characters.'
                ]
            }
        )

    def test_password_more_than_max_length(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '123456789123456789',
            'name': 'Mirabbos',
            'terms': True
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has no more than 16 characters.'
                ]
            }
        )

    def test_unaccepted_terms_checkbox(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '12345678',
            'name': 'Mirabbos',
            'terms': False
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'terms': [
                    'You must accept terms and conditions.'
                ]
            }
        )

    def test_email_already_exists(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '12345678',
            'name': 'Mirabbos',
            'terms': True
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                'email': [
                    'This email address is already being used.'
                ]
            }
        )

    @patch.object(
        target=requests,
        attribute='post',
        side_effect=HTTPError,
    )
    def test_failed_to_send_email(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'existing_email@gmail.com',
            'password': '12345678'
        }
        res = client.post(
            path='/api/exercise/signup/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        user_exists: bool = User.objects.filter(
            email=payload['email']
        ).exists()
        self.assertEqual(
            user_exists,
            False
        )
        self.assertEqual(
            res.status_code,
            503
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Service Unavailable'
            }
        )

# TODO:
#  1) last test did not work,
#  returned "TypeError: test_failed_to_send_email() takes 1 positional argument but 2 were given"


