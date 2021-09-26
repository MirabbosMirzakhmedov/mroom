import datetime
import json
from typing import Dict
from unittest.mock import patch, Mock

import requests
from django.test import TestCase
from django.utils import timezone
from requests.exceptions import HTTPError
from rest_framework.test import APIClient

from mroom import settings
from mroom.api.models import User, Session


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

    def test_successful_signup(self):
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


class TestSignin(TestCase):
    def test_empty_email_field(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': '',
            'password': 'sample_password',
        }
        res = client.post(
            path='/api/signin/',
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
                    'This field may not be blank.'
                ]
            }
        )

    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'invalid_email',
            'password': 'secret_password'
        }
        res = client.post(
            path='/api/signin/',
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

    def test_empty_password_field(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'sample@email.com',
            'password': ''
        }
        res = client.post(
            path='/api/signin/',
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
                'password': [
                    'This field may not be blank.'
                ]
            }
        )

    def test_user_does_not_exist(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'sample@email.com',
            'password': '123456789'
        }
        res = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Incorrect authentication credentials'
            }
        )

    def test_user_exists_wrong_password(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='mirabbos.mirzakhmedov@edu.rtu.lv',
            password='correct_password',
            name='Mirabbos',
            terms=True,
        )
        payload: Dict = {
            'email': user.email,
            'password': 'wrong_password'
        }
        res = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Incorrect authentication credentials'
            }
        )

    def test_successful_signin(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        payload: Dict = {
            'email': user.email,
            'password': 'new_password',
        }
        res = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            200
        )
        self.assertEqual(
            settings.SESSION_COOKIE_NAME in res.cookies,
            True
        )


class TestSignout(TestCase):
    def test_missing_token_cookie(self):
        client: APIClient = APIClient()
        res = client.post(
            path='/api/signout/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Authorization cookie missing'
            }
        )

    def test_session_does_not_exist(self):
        client: APIClient = APIClient()
        client.cookies[settings.SESSION_COOKIE_NAME] = 'test_cookie_token'
        res = client.post(
            path='/api/signout/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Invalid session or inactive user'
            }
        )

    def test_session_expired(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        session: Session = Session.objects.create(
            last_active=datetime.datetime(
                year=2021, month=9, day=10, hour=10,
                minute=20, second=20, microsecond=20
            ),
            user=user,
        )
        session.token = client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = '...'
        res = client.post(
            path='/api/signout/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Invalid session or inactive user'
            }
        )

    def test_successful_signout(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        session: Session = Session.objects.create(
            last_active=timezone.now(),
            user=user,
        )
        client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = session.token
        res = client.post(
            path='/api/signout/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            200
        )
        self.assertEqual(
            res.cookies[
                settings.SESSION_COOKIE_NAME
            ].value,
            ''
        )


class TestCurrentUser(TestCase):
    def test_missing_token_cookie(self):
        client: APIClient = APIClient()
        res = client.post(
            path='/api/current_user/',
            content_type='application/json',
        )

        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Authorization cookie missing'
            }
        )

    def test_session_does_not_exist(self):
        client: APIClient = APIClient()
        client.cookies[settings.SESSION_COOKIE_NAME] = 'test_cookie_token'
        res = client.post(
            path='/api/current_user/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Invalid session or inactive user'
            }
        )

    def test_session_expired(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        session: Session = Session.objects.create(
            last_active=datetime.datetime(
                year=2021, month=9, day=10, hour=10,
                minute=20, second=20, microsecond=20
            ),
            user=user,
        )
        session.token = client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = '...'
        res = client.post(
            path='/api/current_user/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            401
        )
        self.assertEqual(
            res.json(),
            {
                'detail': 'Invalid session or inactive user'
            }
        )

    def test_get_current_user(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        session: Session = Session.objects.create(
            last_active=timezone.now(),
            user=user,
        )
        client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = session.token

        res = client.get(
            path='/api/current_user/',
            content_type='application/json',
        )
        self.assertEqual(
            res.status_code,
            200
        )
        self.assertEqual(
            len(res.data),
            2
        )
        self.assertEqual(
            'uid' and 'name' in res.data,
            True
        )
