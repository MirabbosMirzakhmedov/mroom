from django.test import TestCase
from rest_framework.test import APIClient
from typing import Dict
import json


class TestSignup(TestCase):
    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'invalid_email',
            'password': '12345678'
        }

        res = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json',
        )
        breakpoint()
        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                "email": [
                    "Enter a valid email address."
                ]
            }
        )

    def test_password_less_than_min_length(self):
        client: APIClient = APIClient()
        payload: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '123'
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
                "password": [
                    "Ensure this field has at least 8 characters."
                ]
            }
        )

    def test_password_more_than_max_length(self):
        client: APIClient = APIClient()
        data: Dict = {
            'email': 'willparkerboss@gmail.com',
            'password': '123456789123456789'
        }
        res = client.post(
            path='/api/signup/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )
        self.assertEqual(
            res.json(),
            {
                "password": [
                    "Ensure this field has no more than 16 characters."
                ]
            }
        )
