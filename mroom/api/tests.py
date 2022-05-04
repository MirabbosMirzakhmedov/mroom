import json
from datetime import timedelta
from typing import Dict, List
from unittest.mock import patch, Mock

import requests
from django.conf import settings
from django.test import TestCase
from django.utils import timezone
from requests.exceptions import HTTPError
from rest_framework.test import APIClient

from mroom.api.models import User, Session
from mroom.report.models import Survey

signup_mock = patch.object(
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
        with signup_mock:
            res = client.post(
                path='/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )
            user = User.objects.get(uid=res.json()['uid'])
            survey_exists = Survey.objects.filter(
                key=Survey.DEFAULT,
                user__uid=user.uid,
            ).exists()
        self.assertEqual(survey_exists, True)
        self.assertEqual(
            res.status_code,
            201
        )
        self.assertEqual(
            res.json(),
            {
                'uid': str(user.uid),
                'name': user.name,
                'survey_uid': str(user.surveys.get(key=Survey.DEFAULT).uid)
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


class TestPrivateEndpoint(TestCase):
    paths: List[str] = [
        '/api/current_user/',
        '/api/signout/',
    ]

    def test_missing_token_cookie(self):
        client: APIClient = APIClient()
        for path in self.paths:
            res = client.post(
                path=path,
                content_type='application/json'
            )
            self.assertEqual(
                res.status_code,
                401
            )
            self.assertEqual(
                res.json(),
                {'detail': 'Authorization cookie missing'}
            )

    def test_session_does_not_exist(self):
        client: APIClient = APIClient()
        client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = 'test_cookie_token'

        for path in self.paths:
            res = client.post(
                path=path,
                content_type='application/json',
            )
            self.assertEqual(
                res.status_code,
                401
            )
            self.assertEqual(
                res.json(),
                {'detail': 'Invalid session or inactive user'}
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
            user=user,
        )
        client.cookies[settings.SESSION_COOKIE_NAME] = session.token
        session.last_active = timezone.now() - timedelta(days=400)
        session.save()
        for path in self.paths:
            res = client.post(
                path=path,
                content_type='application/json',
            )
            self.assertEqual(
                res.status_code,
                401
            )
            self.assertEqual(
                res.json(),
                {'detail': 'Invalid session or inactive user'}
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
            user=user,
            is_active=True,
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

    def test_get_current_user(self):
        client: APIClient = APIClient()
        payload_signup: Dict = {
            'email': 'mirabbos.dov@gmail.com',
            'password': '123456789',
            'name': 'Mirabbos',
            'terms': True
        }
        with signup_mock:
            res = client.post(
                path='/api/signup/',
                data=json.dumps(payload_signup),
                content_type='application/json'
            )
        user = User.objects.get(uid=res.json()['uid'])
        session: Session = Session.objects.create(
            user=user,
            is_active=True,
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
            3
        )
        self.assertEqual(
            str(user.uid),
            res.data['uid']
        )
        self.assertEqual(
            user.name,
            res.data['name']
        )
        self.assertIsNotNone(
            res.data['survey_uid']
        )


class TestBarber(TestCase):
    def test_get_list_of_barbers(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            name='Alexis',
            email='alexis_barber@gmail.com',
            terms=True
        )
        user.is_barber = True
        user.save()
        res = client.get(
            path='/api/barber/',
            content_type='application/json',
        )
        self.assertEqual(
            res.json(),
            [
                {'uid': str(user.uid),
                 'name': user.name}
            ]
        )
        self.assertEqual(
            res.status_code,
            200
        )

    def test_unsuccessful(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            name='Sonia',
            email='sonia_user@gmail.com',
            terms=True
        )
        user.is_barber = False
        user.save()
        res = client.get(
            path='/api/barber/',
            content_type='application/json',
        )
        self.assertEqual(
            res.json(),
            []
        )
        self.assertEqual(
            res.status_code,
            200
        )


class TestAppointment(TestCase):
    def test_empty_full_name(self):
        client: APIClient = APIClient()
        barber: User = User.objects.create_user(
            name='John Lewis',
            email='john_lewis@gmail.com',
            terms=True
        )
        barber.is_barber = True
        barber.save()
        payload: Dict = {
            'name': '',
            'phone_number': '+3712008080',
            'barber': str(barber.uid),
            'message': 'Your message',
            'date': '2021-10-26T02:17'
        }
        res = client.post(
            path='/api/appointment/',
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
                'name': ['This field may not be blank.'],
                'date': ['Cannot insert date in the past.']
            }
        )

    def test_empty_phone_number(self):
        client: APIClient = APIClient()
        barber: User = User.objects.create_user(
            name='John Lewis',
            email='john_lewis@gmail.com',
            terms=True
        )
        barber.is_barber = True
        barber.save()
        payload: Dict = {
            'name': 'John Lewis',
            'phone_number': '',
            'barber': str(barber.uid),
            'message': 'Your message',
            'date': '2021-10-26T02:17'
        }
        res = client.post(
            path='/api/appointment/',
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
                'phone_number': ['This field may not be blank.'],
                'date': ['Cannot insert date in the past.']
            }
        )

    def test_phone_number_min_length(self):
        client: APIClient = APIClient()
        barber: User = User.objects.create_user(
            name='John Lewis',
            email='john_lewis@gmail.com',
            terms=True
        )
        barber.is_barber = True
        barber.save()
        payload: Dict = {
            'name': 'Alex Costa',
            'phone_number': '+20030',
            'barber': str(barber.uid),
            'message': 'Your message',
            'date': '2021-10-26T02:17'
        }
        res = client.post(
            path='/api/appointment/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.json(),
            {
                'phone_number': [
                    'Phone number must be between 9 - 15 '
                    'digits and cannot have blank spaces.'
                ],
                'date': [
                    'Cannot insert date in the past.'
                ]
            }
        )
        self.assertEqual(
            res.status_code,
            400
        )

    def test_phone_number_with_spaces(self):
        client: APIClient = APIClient()
        barber: User = User.objects.create_user(
            name='John Lewis',
            email='john_lewis@gmail.com',
            terms=True
        )
        barber.is_barber = True
        barber.save()
        payload: Dict = {
            'name': 'Alex Costa',
            'phone_number': '+371 200 30 700',
            'barber': str(barber.uid),
            'message': 'Your message',
            'date': '2021-10-26T02:17'
        }
        res = client.post(
            path='/api/appointment/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(
            res.json(),
            {
                'phone_number': [
                    'Phone number must be between 9 - 15 '
                    'digits and cannot have blank spaces.'
                ],
                'date': ['Cannot insert date in the past.']
            }
        )
        self.assertEqual(
            res.status_code,
            400
        )

    def test_appointment_successful(self):
        client: APIClient = APIClient()
        barber: User = User.objects.create_user(
            name='John Lewis',
            email='john_lewis@gmail.com',
            terms=True
        )
        barber.is_barber = True
        barber.save()

        appointment_date: str = (
                timezone.now() + timedelta(days=1)
        ).strftime('%Y-%m-%dT%H:%M')

        payload: Dict = {
            'name': 'Alex Costa',
            'phone_number': '+3712008080',
            'barber': str(barber.uid),
            'message': 'Your message',
            'date': appointment_date,
        }
        res = client.post(
            path='/api/appointment/',
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
                'name': 'Alex Costa',
                'phone_number': '+3712008080',
                'date': appointment_date,
                'barber': str(barber.uid),
                'message': 'Your message'
            }
        )
