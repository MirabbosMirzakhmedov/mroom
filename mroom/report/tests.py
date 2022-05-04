import json
from typing import Dict

from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from mroom.api.models import User
from mroom.api.tests import signup_mock
from mroom.report.models import Survey


class TestSurvey(TestCase):
    def test_get_single_survey(self):
        client: APIClient = APIClient()
        payload_signup: Dict = {
            'email': 'mirabbos.dov@gmail.com',
            'password': '123456789',
            'name': 'Mirabbos',
            'terms': True
        }
        payload_signin: Dict = {
            'email': payload_signup['email'],
            'password': payload_signup['password']
        }
        with signup_mock:
            res = client.post(
                path='/api/signup/',
                data=json.dumps(payload_signup),
                content_type='application/json'
            )
        user = User.objects.get(uid=res.json()['uid'])
        res = client.post(
            path='/api/signin/',
            data=json.dumps(payload_signin),
            content_type='application/json'
        )
        self.assertEqual(
            user.sessions.filter(is_active=True).exists(),
            True
        )
        active_session = user.sessions.filter(is_active=True).first()
        client.cookies[settings.SESSION_COOKIE_NAME] = active_session.token
        survey = user.surveys.filter(
            key=Survey.DEFAULT,
        ).first()
        res = client.get(
            path=f'/api/survey/{str(survey.uid)}/',
            content_type='application/json'
        )
        self.assertEqual(
            res.json(),
            {
                'user': {
                    'uid': str(user.uid),
                    'name': str(user.name),
                    'survey_uid': str(survey.uid),
                },
                'questions': [
                    {
                        'answers': [
                            {
                                'name': 'Very short',
                                'description': 'Very_short',
                                'key': 'very_short'
                            },
                            {
                                'name': 'Short',
                                'description': 'Short',
                                'key': 'short'
                            },
                            {
                                'name': 'Medium',
                                'description': 'Medium',
                                'key': 'medium'
                            },
                            {
                                'name': 'Long',
                                'description': 'Long',
                                'key': 'long'
                            }
                        ],
                        'solutions': [

                        ]
                    },
                    {
                        'answers': [
                            {
                                'name': 'Everyday',
                                'description': 'Everyday',
                                'key': 'everyday'
                            },
                            {
                                'name': '2 times a week',
                                'description': '2_times_a_week',
                                'key': 'two_times'
                            },
                            {
                                'name': '1 time a week',
                                'description': '1_time_a_week',
                                'key': 'one_time'
                            },
                            {
                                'name': '3 times a week',
                                'description': '3_times_a_wee',
                                'key': 'three_times'
                            }
                        ],
                        'solutions': [

                        ]
                    },
                    {
                        'answers': [
                            {
                                'name': 'Dandruff',
                                'description': 'Dandruff',
                                'key': 'dandruff'
                            },
                            {
                                'name': 'Hair loss',
                                'description': 'Hair_loss',
                                'key': 'hair_loss'
                            },
                            {
                                'name': 'Dry hair',
                                'description': 'Dry_hair',
                                'key': 'dry_hair'
                            },
                            {
                                'name': 'Psoriasis',
                                'description': 'Psoriasis',
                                'key': 'psoriasis'
                            },
                            {
                                'name': 'Head lice',
                                'description': 'Head_lice',
                                'key': 'head_lice'
                            },
                            {
                                'name': 'Bamboo hair',
                                'description': 'Bamboo_hair',
                                'key': 'bamboo_hair'
                            },
                            {
                                'name': 'Very oily hair',
                                'description': 'Very_oily_hair',
                                'key': 'very_oily'
                            }
                        ],
                        'solutions': [

                        ]
                    },
                    {
                        'answers': [
                            {
                                'name': 'EUR',
                                'description': 'EUR',
                                'key': 'eur'
                            },
                            {
                                'name': 'USD',
                                'description': 'USD',
                                'key': 'usd'
                            }
                        ],
                        'solutions': [

                        ]
                    },
                    {
                        'answers': [
                            {
                                'name': 'Yes',
                                'description': 'Yes',
                                'key': 'yes'
                            },
                            {
                                'name': 'No',
                                'description': 'No',
                                'key': 'no'
                            },
                            {
                                'name': "I don't know",
                                'description': "I don't know",
                                'key': 'idk'
                            }
                        ],
                        'solutions': [
                            {
                                'name': 'Applying aloe liquid',
                                'description': 'Applying_aloe_liquid',
                                'key': 'aloe_liquid'
                            },
                            {
                                'name': 'Applying lemon',
                                'description': 'Applying_lemon',
                                'key': 'lemon'
                            },
                            {
                                'name': 'Applying garlic water',
                                'description': 'Applying_garlic_water',
                                'key': 'garlic_water'
                            },
                            {
                                'name': 'Do not washing',
                                'description': 'Do_not_washing',
                                'key': 'not_washing'
                            }
                        ]
                    }
                ]
            }
        )
        self.assertEqual(
            res.status_code,
            200
        )
