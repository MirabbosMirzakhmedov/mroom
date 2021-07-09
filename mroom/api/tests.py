import json
from typing import Dict
from unittest.mock import patch, Mock

import requests
from django.test import TestCase
from requests.exceptions import HTTPError
from rest_framework.test import APIClient

from mroom.api.models import User


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
        email: str = 'willparkerboss@gmail.com'
        password: str = '123456789'
        name: str = 'Mirabbos Mirzakhmedov'
        terms: bool = True
        User.objects.create_user(
            email=email,
            password=password,
            name=name,
            terms=terms
        )
        payload: Dict = {
            'email': email,
            'password': password,
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

    def test_failed_to_send_email(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'existing_email@gmail.com',
            'password': '123456789',
            'name': 'Mirabbos',
            'terms': True
        }
        res_mock = patch.object(
            target=requests,
            attribute='post',
            side_effect=[
                HTTPError
            ]
        )
        with res_mock:
            res = client.post(
                path='/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
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

    def test_successful_signup(self, *args, **kwargs):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'mirabbos.dov@gmail.com',
            'password': '123456789',
            'name': 'Mirabbos',
            'terms': True
        }
        res_mock = patch.object(
            target=requests,
            attribute='post',
            side_effect=[
                Mock(
                    **{
                        'status_code': 200,
                        'json.return_value': {
                            'contact_id': '09540eaf-6ee8-427c-803d-606c5e299bb3'
                        }
                    }
                )
            ]
        )
        with res_mock:
            res = client.post(
                path='/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )
        self.assertEqual(
            res.status_code,
            201
        )
        self.assertEqual(
            res.json(),
            {
                'detail': f'Signup was successful, '
                          f'registration email was sent to {payload["email"]}'
            }
        )
        self.assertEqual(
            User.objects.filter(email=payload['email']).exists(),
            True
        )
