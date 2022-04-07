from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from mroom.api.models import User, Session
from mroom.report.models import Question, Answer, Survey


class TestSurvey(TestCase):
    # GET endpoint
    def test_get_survey(self):
        client: APIClient = APIClient()
        user: User = User.objects.create_user(
            email='new_email@gmail.com',
            password='new_password',
            name='Mirabbos',
            terms=True,
        )
        # Creating a session
        session: Session = Session.objects.create(
            user=user,
            is_active=True,
        )
        client.cookies[
            settings.SESSION_COOKIE_NAME
        ] = session.token

        # CREATING ANSWERS
        # 1.1
        first_answer_very_short = Answer.objects.create(
            name='Very short',
            description='Very_short',
            key=Answer.VERY_SHORT
        )
        # 1.2
        first_answer_short = Answer.objects.create(
            name='Short',
            description='Short',
            key=Answer.SHORT
        )
        # 1.3
        first_answer_medium = Answer.objects.create(
            name='Medium',
            description='Medium',
            key=Answer.MEDIUM
        )
        # 1.4
        first_answer_long = Answer.objects.create(
            name='Long',
            description='Long',
            key=Answer.LONG
        )

        # 2.1
        second_answer_everyday = Answer.objects.create(
            name='Everyday',
            description='Everyday',
            key=Answer.EVERYDAY
        )
        # 2.2
        second_answer_two_times = Answer.objects.create(
            name='2 times a week',
            description='2_times_a_week',
            key=Answer.TWO_TIMES
        )
        # 2.3
        second_answer_one_time = Answer.objects.create(
            name='1 time a week',
            description='1_time_a_week',
            key=Answer.ONE_TIME
        )
        # 2.4
        second_answer_three_times = Answer.objects.create(
            name='3 times a week',
            description='3_times_a_week',
            key=Answer.THREE_TIMES
        )

        # 3.1
        third_answer_dandruff = Answer.objects.create(
            name='Dandruff',
            description='Dandruff',
            key=Answer.DANDRUFF
        )

        # 3.2
        third_answer_hair_loss = Answer.objects.create(
            name='Hair loss',
            description='Hair_loss',
            key=Answer.HAIR_LOSS
        )

        # 3.3
        third_answer_dry_hair = Answer.objects.create(
            name='Dry hair',
            description='Dry_hair',
            key=Answer.DRY_HAIR
        )

        # 3.4
        third_answer_psoriasis = Answer.objects.create(
            name='Psoriasis',
            description='Psoriasis',
            key=Answer.PSORIASIS
        )

        # 3.5
        third_answer_head_lice = Answer.objects.create(
            name='Head lice',
            description='Head_lice',
            key=Answer.HEAD_LICE
        )

        # 3.6
        third_answer_bamboo_hair = Answer.objects.create(
            name='Bamboo hair',
            description='Bamboo_hair',
            key=Answer.BAMBOO_HAIR
        )

        # 3.7
        third_answer_very_oily_hair = Answer.objects.create(
            name='Very oily hair',
            description='Very_oily_hair',
            key=Answer.VERY_OILY_HAIR
        )

        # 4.1
        fourth_answer_euro = Answer.objects.create(
            name='EUR',
            description='EUR',
            key=Answer.EUR
        )
        # 4.2
        fourth_answer_usd = Answer.objects.create(
            name='USD',
            description='USD',
            key=Answer.USD
        )

        # 5.1
        fifth_answer_yes = Answer.objects.create(
            name='Yes',
            description='Yes',
            key=Answer.CHOICE_YES
        )
        # 5.2
        fifth_answer_no = Answer.objects.create(
            name='No',
            description='No',
            key=Answer.CHOICE_NO
        )
        # 5.3
        fifth_answer_idk = Answer.objects.create(
            name="I don't know",
            description="I don't know",
            key=Answer.CHOICE_I_DONT_KNOW
        )
        # 5.4
        fifth_answer_yes_aloe_liquid = Answer.objects.create(
            name='Applying aloe liquid',
            description='Applying_aloe_liquid',
            key=Answer.CHOICE_YES_ALOE_LIQUID
        )
        # 5.5
        fifth_answer_yes_lemon = Answer.objects.create(
            name='Applying lemon',
            description='Applying_lemon',
            key=Answer.CHOICE_YES_LEMON
        )
        # 5.6
        fifth_answer_yes_garlic_water = Answer.objects.create(
            name='Applying garlic water',
            description='Applying_garlic_water',
            key=Answer.CHOICE_YES_GARLIC
        )
        # 5.7
        fifth_answer_yes_not_washing = Answer.objects.create(
            name='Do not washing',
            description='Do_not_washing',
            key=Answer.CHOICE_YES_NOT_WASHING
        )

        # CREATING QUESTIONS
        # Question 1
        question_one = Question.objects.create(
            name='How long hair do you have?'
        )
        question_one.answers.add(
            first_answer_very_short, first_answer_short,
            first_answer_medium, first_answer_long
        )

        # Question 2
        question_two = Question.objects.create(
            name='How often do you wash your hair?'
        )
        question_two.answers.add(
            second_answer_everyday, second_answer_two_times,
            second_answer_one_time, second_answer_three_times,
        )

        # Question 3
        question_three = Question.objects.create(
            name='What kind of problems do you have?'
        )
        question_three.answers.add(
            third_answer_dandruff, third_answer_hair_loss,
            third_answer_dry_hair, third_answer_psoriasis,
            third_answer_head_lice, third_answer_bamboo_hair,
            third_answer_very_oily_hair
        )

        # Question 4
        question_four = Question.objects.create(
            name='What is the price for your shampoo?'
        )
        question_four.answers.add(
            fourth_answer_euro, fourth_answer_usd,
        )

        # Question 5
        question_five = Question.objects.create(
            name='Solutions you can do at home'
        )
        question_five.answers.add(
            fifth_answer_yes, fifth_answer_no, fifth_answer_idk,
        )
        question_five.solutions.add(
            fifth_answer_yes_aloe_liquid, fifth_answer_yes_lemon,
            fifth_answer_yes_garlic_water, fifth_answer_yes_not_washing
        )

        # Creating a survey
        survey = Survey.objects.create(user=user)
        survey.questions.add(
            question_one, question_two,
            question_three, question_four,
            question_five
        )

        res = client.get(
            path='/api/survey/',
            content_type='application/json',
        )
        self.assertEqual(
            res.json(),
            [
                {
                    "user": {
                        "uid": str(user.uid),
                        "name": user.name
                    },
                    "questions": [
                        {
                            "answers": [
                                {
                                    "name": "Very short",
                                    "description": "Very_short",
                                    "key": "very_short"
                                },
                                {
                                    "name": "Short",
                                    "description": "Short",
                                    "key": "short"
                                },
                                {
                                    "name": "Medium",
                                    "description": "Medium",
                                    "key": "medium"
                                },
                                {
                                    "name": "Long",
                                    "description": "Long",
                                    "key": "long"
                                }
                            ],
                            "solutions": [

                            ]
                        },
                        {
                            "answers": [
                                {
                                    "name": "Everyday",
                                    "description": "Everyday",
                                    "key": "everyday"
                                },
                                {
                                    "name": "2 times a week",
                                    "description": "2_times_a_week",
                                    "key": "two_times"
                                },
                                {
                                    "name": "1 time a week",
                                    "description": "1_time_a_week",
                                    "key": "one_time"
                                },
                                {
                                    "name": "3 times a week",
                                    "description": "3_times_a_week",
                                    "key": "three_times"
                                }
                            ],
                            "solutions": [

                            ]
                        },
                        {
                            "answers": [
                                {
                                    "name": "Dandruff",
                                    "description": "Dandruff",
                                    "key": "dandruff"
                                },
                                {
                                    "name": "Hair loss",
                                    "description": "Hair_loss",
                                    "key": "hair_loss"
                                },
                                {
                                    "name": "Dry hair",
                                    "description": "Dry_hair",
                                    "key": "dry_hair"
                                },
                                {
                                    "name": "Psoriasis",
                                    "description": "Psoriasis",
                                    "key": "psoriasis"
                                },
                                {
                                    "name": "Head lice",
                                    "description": "Head_lice",
                                    "key": "head_lice"
                                },
                                {
                                    "name": "Bamboo hair",
                                    "description": "Bamboo_hair",
                                    "key": "bamboo_hair"
                                },
                                {
                                    "name": "Very oily hair",
                                    "description": "Very_oily_hair",
                                    "key": "very_oily"
                                }
                            ],
                            "solutions": [

                            ]
                        },
                        {
                            "answers": [
                                {
                                    "name": "EUR",
                                    "description": "EUR",
                                    "key": "eur"
                                },
                                {
                                    "name": "USD",
                                    "description": "USD",
                                    "key": "usd"
                                }
                            ],
                            "solutions": [

                            ]
                        },
                        {
                            "answers": [
                                {
                                    "name": "Yes",
                                    "description": "Yes",
                                    "key": "yes"
                                },
                                {
                                    "name": "No",
                                    "description": "No",
                                    "key": "no"
                                },
                                {
                                    "name": "I don't know",
                                    "description": "I don't know",
                                    "key": "idk"
                                }
                            ],
                            "solutions": [
                                {
                                    "name": "Applying aloe liquid",
                                    "description": "Applying_aloe_liquid",
                                    "key": "aloe_liquid"
                                },
                                {
                                    "name": "Applying lemon",
                                    "description": "Applying_lemon",
                                    "key": "lemon"
                                },
                                {
                                    "name": "Applying garlic water",
                                    "description": "Applying_garlic_water",
                                    "key": "garlic_water"
                                },
                                {
                                    "name": "Do not washing",
                                    "description": "Do_not_washing",
                                    "key": "not_washing"
                                }
                            ]
                        }
                    ]
                }
            ]
        )
        self.assertEqual(
            res.status_code,
            200
        )

# TODO:
#  1) Answer, Question and Survey creation -> Custom migrations
